import streamlit as st

def show(low_bandwidth):
    st.header("Preventive Care")
    
    if low_bandwidth:
        topic = st.selectbox("Select health topic", 
                           ["Malaria", "Hygiene", "Nutrition", "Vaccination", 
                            "Safe Water", "Exercise", "Mental Health"])
        
        if topic == "Malaria":
            st.subheader("Malaria Prevention")
            st.write("1. Sleep under insecticide-treated nets (ITNs)")
            st.write("2. Use mosquito repellents (DEET, picaridin)")
            st.write("3. Wear long sleeves/pants at dusk/dawn")
            st.write("4. Eliminate standing water near home")
            st.write("5. Take prophylactic medication in high-risk areas")
            st.info("Seek immediate testing if fever develops")
            
        elif topic == "Hygiene":
            st.subheader("Basic Hygiene Practices")
            st.write("1. Wash hands with soap for 20 seconds:")
            st.write("   - Before eating")
            st.write("   - After toilet use")
            st.write("   - After touching animals")
            st.write("2. Brush teeth twice daily with fluoride toothpaste")
            st.write("3. Bathe regularly with clean water")
            st.write("4. Keep nails trimmed and clean")
            st.write("5. Properly dispose of waste")
            
        elif topic == "Nutrition":
            st.subheader("Healthy Eating Guidelines")
            st.write("1. Eat variety of foods daily:")
            st.write("   - Fruits/vegetables (5 servings)")
            st.write("   - Whole grains")
            st.write("   - Protein (beans, eggs, meat)")
            st.write("2. Limit salt, sugar, and oily foods")
            st.write("3. Drink 8 glasses of clean water daily")
            st.write("4. Breastfeed infants exclusively for 6 months")
            st.write("5. Practice safe food handling")
            
        elif topic == "Vaccination":
            st.subheader("Essential Vaccines")
            st.write("1. Children should receive:")
            st.write("   - BCG (TB)")
            st.write("   - Polio drops")
            st.write("   - DPT (diphtheria/pertussis/tetanus)")
            st.write("   - Measles vaccine")
            st.write("2. Adults need:")
            st.write("   - Tetanus boosters (every 10 years)")
            st.write("   - COVID-19 vaccines")
            st.write("3. Special vaccines for:")
            st.write("   - Hepatitis B")
            st.write("   - HPV (cervical cancer prevention)")
            st.info("Check local vaccination schedule")
            
        elif topic == "Safe Water":
            st.subheader("Water Safety Practices")
            st.write("1. Always drink from protected sources")
            st.write("2. Boil water for 1 minute if unsafe")
            st.write("3. Use water filters or chlorine tablets")
            st.write("4. Store water in clean, covered containers")
            st.write("5. Wash hands before handling drinking water")
            st.warning("Seek treatment for diarrhea immediately")
            
        elif topic == "Exercise":
            st.subheader("Physical Activity Guidelines")
            st.write("1. Adults: 30 minutes daily")
            st.write("   - Walking, gardening, dancing")
            st.write("2. Children: 60 minutes daily play")
            st.write("3. Include strength training 2x/week")
            st.write("4. Take breaks from sitting")
            st.write("5. Start slow if new to exercise")
            st.info("Even small activity is better than none")
            
        elif topic == "Mental Health":
            st.subheader("Emotional Wellbeing Tips")
            st.write("1. Maintain social connections")
            st.write("2. Get 7-9 hours of sleep")
            st.write("3. Practice stress relief:")
            st.write("   - Deep breathing")
            st.write("   - Meditation/prayer")
            st.write("4. Limit alcohol/drugs")
            st.write("5. Seek help for persistent sadness/anxiety")
            st.error("Reach out if having suicidal thoughts")
            
    else:
        # Your existing normal bandwidth code
        st.video("https://youtu.be/XMcab1MFaLc?si=BmDLqkqdXQssJJzt")