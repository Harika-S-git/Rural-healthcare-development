import streamlit as st

def show(low_bandwidth):
    st.header("Symptom Analysis")
    
    # Disease database with symptoms and recommendations
    DISEASE_DB = {
        "Common Cold": {
            "symptoms": ["runny nose", "sneezing", "cough", "sore throat"],
            "medicine": "Paracetamol 500mg every 6 hours (for fever), Antihistamines",
            "advice": "Rest, drink warm fluids, use saline nasal drops"
        },
        "Flu (Influenza)": {
            "symptoms": ["fever", "body aches", "fatigue", "dry cough", "headache"],
            "medicine": "Oseltamivir 75mg twice daily for 5 days (if started within 48 hours), Paracetamol for fever",
            "advice": "Stay hydrated, rest, and isolate to prevent spreading"
        },
        "Malaria": {
            "symptoms": ["high fever", "chills", "headache", "sweating", "nausea"],
            "medicine": "Artemisinin-based combination therapy (ACT) as prescribed",
            "advice": "Seek immediate medical attention - can be life-threatening"
        },
        "Dengue Fever": {
            "symptoms": ["high fever", "severe headache", "eye pain", "rash", "muscle pain"],
            "medicine": "Paracetamol ONLY (NO aspirin/ibuprofen), maintain hydration",
            "advice": "Monitor platelet count, watch for warning signs like bleeding"
        },
        "Typhoid Fever": {
            "symptoms": ["prolonged fever", "headache", "stomach pain", "constipation or diarrhea"],
            "medicine": "Ciprofloxacin 500mg twice daily or Azithromycin 1g daily for 5-7 days",
            "advice": "Boil drinking water, practice strict hygiene, complete full antibiotic course"
        },
        "UTI (Urinary Tract Infection)": {
            "symptoms": ["burning urination", "frequent urination", "lower abdominal pain"],
            "medicine": "Ciprofloxacin 250mg twice daily for 3 days or Nitrofurantoin 100mg twice daily for 5 days",
            "advice": "Drink plenty of water, avoid holding urine"
        }
    }

    # Low-bandwidth mode (text-based)
    if low_bandwidth:
        st.markdown("*Describe all your symptoms in simple words:*")
        symptom_text = st.text_area("For example: 'I have fever and headache since yesterday'", 
                                 height=100)
        
        if st.button("Analyze Symptoms"):
            if not symptom_text.strip():
                st.warning("Please describe your symptoms")
                return
            
            # Convert to lowercase for easier matching
            user_input = symptom_text.lower()
            
            # Emergency symptoms check
            emergency_keywords = [
                "difficulty breathing", "chest pain", "severe bleeding",
                "unconscious", "severe headache", "high fever",
                "can't wake up", "severe dehydration"
            ]
            if any(keyword in user_input for keyword in emergency_keywords):
                st.error("""
                🚨 EMERGENCY WARNING!
                You may need immediate medical care.
                Please contact your local emergency services or go to the nearest hospital.
                """)
                return
            
            # Check for symptom patterns
            matched_conditions = []
            for condition, data in DISEASE_DB.items():
                symptom_matches = sum(
                    1 for symptom in data["symptoms"] 
                    if symptom in user_input
                )
                if symptom_matches >= 2:  # At least 2 matching symptoms
                    matched_conditions.append((condition, symptom_matches, data))
            
            if matched_conditions:
                # Sort by best match
                matched_conditions.sort(key=lambda x: x[1], reverse=True)
                best_match = matched_conditions[0][2]  # Get the data dict
                
                st.markdown(f"*Possible condition:* {matched_conditions[0][0]}")
                st.markdown(f"*Common symptoms:* {', '.join(best_match['symptoms'])}")
                st.markdown(f"*Self-care advice:* {best_match['advice']}")
                
                # Show medicine with precautions
                st.markdown("*Medicine suggestions:*")
                st.info(best_match['medicine'])
                st.warning("""
                Important: 
                - These are general recommendations only
                - Consult a doctor before taking any medicine
                - Complete the full course if taking antibiotics
                """)
                
                st.markdown("*When to seek help:*")
                st.error("""
                Contact a healthcare provider if:
                - Symptoms worsen or last more than 3 days
                - You develop high fever (above 102°F/39°C)
                - You experience severe symptoms
                """)
            else:
                st.info("""
                No specific condition identified based on your symptoms.
                General advice:
                - Rest and drink plenty of fluids
                - Monitor your symptoms
                - Seek medical help if:
                  * Symptoms last more than 3 days
                  * You develop fever
                  * You feel worse
                """)
    
    # Normal mode (interactive)
    else:
        col1, col2 = st.columns(2)
        with col1:
            symptoms = st.multiselect("Select all your symptoms",
                                    ["Fever", "Cough", "Headache", 
                                     "Body aches", "Runny nose", 
                                     "Sore throat", "Chills", "Sweating",
                                     "Nausea", "Vomiting", "Diarrhea",
                                     "Burning urination", "Frequent urination",
                                     "Rash", "Eye pain", "Stomach pain"])
        with col2:
            duration = st.selectbox("How long have you had these symptoms?",
                                  ["Less than 1 day", "1-3 days", 
                                   "4-7 days", "More than 1 week"])
            severity = st.radio("How severe are your symptoms?", 
                              ["Mild", "Moderate", "Severe"])
            age_group = st.selectbox("Age group",
                                   ["Under 12", "12-18", "19-40", "41-65", "65+"])
        
        if st.button("Get Detailed Analysis"):
            if not symptoms:
                st.warning("Please select at least one symptom")
                return
                
            # Convert symptoms to lowercase for matching
            user_symptoms = [s.lower() for s in symptoms]
            
            # Emergency check for normal mode
            emergency_symptoms = {
                "difficulty breathing": "Respiratory emergency",
                "chest pain": "Possible heart problem",
                "severe headache": "Could indicate meningitis",
                "high fever": "May indicate serious infection"
            }
            
            urgent_cases = []
            for symptom, message in emergency_symptoms.items():
                if symptom in user_symptoms and severity == "Severe":
                    urgent_cases.append(message)
            
            if urgent_cases:
                st.error(f"""
                🚨 URGENT MEDICAL ATTENTION NEEDED!
                Possible {', '.join(urgent_cases)}
                Please seek immediate medical care.
                """)
                return
            
            # Match symptoms to possible conditions
            matched_conditions = []
            for condition, data in DISEASE_DB.items():
                symptom_matches = sum(
                    1 for symptom in data["symptoms"] 
                    if symptom in user_symptoms
                )
                if symptom_matches >= 2:  # At least 2 matching symptoms
                    matched_conditions.append((condition, symptom_matches, data))
            
            if matched_conditions:
                # Sort by best match
                matched_conditions.sort(key=lambda x: x[1], reverse=True)
                
                st.subheader("Possible Conditions:")
                for i, (condition, count, data) in enumerate(matched_conditions[:3]):  # Show top 3
                    with st.expander(f"{i+1}. {condition} ({count}/{len(data['symptoms'])} symptoms matched)"):
                        st.markdown(f"*Common symptoms:* {', '.join(data['symptoms'])}")
                        st.markdown(f"*Recommended medicine:* {data['medicine']}")
                        st.markdown(f"*Self-care advice:* {data['advice']}")
                        
                        # Special considerations
                        if condition == "Dengue Fever":
                            st.warning("""
                            DENGUE WARNING:
                            - Monitor platelet count daily
                            - Watch for bleeding gums or nosebleeds
                            - Hospitalization may be needed if severe
                            """)
                        elif condition == "Malaria":
                            st.warning("""
                            MALARIA WARNING:
                            - Can progress rapidly to severe illness
                            - Requires blood test confirmation
                            - Complete all prescribed medication
                            """)
                
                # General advice
                st.subheader("General Recommendations:")
                if severity == "Mild" and duration in ["Less than 1 day", "1-3 days"]:
                    st.info("""
                    Your condition appears mild:
                    - Try self-care measures first
                    - Monitor for worsening symptoms
                    - Consider teleconsultation if available
                    """)
                else:
                    st.warning("""
                    Based on symptom duration/severity:
                    - Recommended to consult a healthcare provider
                    - Complete any prescribed treatment
                    - Watch for warning signs
                    """)
                
                # Age-specific advice
                if age_group in ["Under 12", "65+"]:
                    st.warning(f"""
                    SPECIAL NOTE FOR {age_group}:
                    - More vulnerable to complications
                    - Recommended to consult doctor sooner
                    - May need adjusted medication doses
                    """)
                
            else:
                st.info("""
                No specific condition identified matching all your symptoms.
                General advice:
                - Rest and stay hydrated
                - Monitor for new or worsening symptoms
                - Consider consulting if:
                  * Symptoms persist beyond 3 days
                  * Fever develops or increases
                  * You feel generally unwell
                """)
                
                # Common over-the-counter suggestions
                if "fever" in user_symptoms or "body aches" in user_symptoms:
                    st.markdown("*For fever/pain relief:*")
                    st.info("""
                    - Paracetamol 500mg every 6 hours (max 4 doses/day)
                    - Avoid aspirin in children/teens
                    - Ibuprofen may be used in adults unless contraindicated
                    """)