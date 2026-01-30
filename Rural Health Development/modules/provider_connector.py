import streamlit as st
import time
import random

def show(low_bandwidth):
    st.header("Connect with Healthcare Providers")
    
    # Doctor database - village to doctors mapping
    DOCTORS_DB = {
        "Village A": [
            {"name": "Dr. Sharma", "distance": "3km", "specialty": "General Physician", "contact": "98765-43210"},
            {"name": "Dr. Patel", "distance": "5km", "specialty": "Pediatrician", "contact": "98765-43211"}
        ],
        "Village B": [
            {"name": "Dr. Khan", "distance": "2km", "specialty": "Cardiologist", "contact": "98765-43212"},
            {"name": "Dr. Gupta", "distance": "7km", "specialty": "Dermatologist", "contact": "98765-43213"}
        ]
    }
    
    # Emergency services database
    EMERGENCY_SERVICES = {
        "Village A": {
            "Ambulance": "108",
            "Police": "100",
            "Fire": "101",
            "Women's Helpline": "1091"
        },
        "Village B": {
            "Ambulance": "108",
            "Police": "100",
            "Fire": "101",
            "Poison Control": "1800-111-222"
        }
    }
    
    location = st.selectbox("Select your nearest location", list(DOCTORS_DB.keys()))
    
    if st.button("Find Available Doctors"):
        # Clear previous results
        st.empty()
        
        # Get doctors for selected location
        available_doctors = DOCTORS_DB.get(location, [])
        
        if available_doctors:
            st.success(f"Found {len(available_doctors)} doctors near {location}:")
            
            for doctor in available_doctors:
                with st.expander(f"{doctor['name']} ({doctor['distance']} away)"):
                    st.write(f"**Specialty:** {doctor['specialty']}")
                    st.write(f"**Contact:** {doctor['contact']}")
                    st.write(f"**Estimated travel time:** {random.randint(5, 15)} minutes")
                    
                    if not low_bandwidth:
                        if st.button(f"Request callback from {doctor['name']}", 
                                   key=f"callback_{doctor['name']}"):
                            with st.spinner("Connecting you to the doctor..."):
                                time.sleep(2)  # Simulate connection delay
                            st.balloons()
                            st.success(f"✅ {doctor['name']}'s assistant will call you within 15 minutes at {doctor['contact']}!")
        else:
            st.warning(f"No doctors found in {location}. Try searching nearby villages.")
    
    # Emergency contact information
    st.markdown("---")
    st.subheader("🚨 Emergency Services")
    
    emergency_col1, emergency_col2 = st.columns(2)
    
    with emergency_col1:
        st.markdown("**Standard Emergency Numbers**")
        st.write(f"Ambulance: {EMERGENCY_SERVICES[location]['Ambulance']}")
        st.write(f"Police: {EMERGENCY_SERVICES[location]['Police']}")
        
    with emergency_col2:
        st.markdown("**Specialized Help**")
        for service, number in EMERGENCY_SERVICES[location].items():
            if service not in ["Ambulance", "Police"]:  # Already shown in col1
                st.write(f"{service}: {number}")
    
    st.warning("Call these numbers immediately in case of emergencies!")