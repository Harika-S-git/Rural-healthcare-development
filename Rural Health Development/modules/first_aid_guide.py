import streamlit as st

# ---------------- AI LOGIC ---------------- #
def generate_ai_first_aid(condition, age, setting):
    condition = condition.lower()

    # Snake Bite
    if "snake" in condition:
        return [
            "Keep the person calm and still. Do not let them walk.",
            "Do NOT cut the wound or try to suck the venom.",
            "Immobilize the bitten limb using a stick or cloth.",
            "Remove rings, bangles, or tight clothing near the bite.",
            "Keep the bitten part below heart level.",
            "Give clean water if the person is awake.",
            "Arrange transport to the nearest hospital immediately."
        ]

    # Burns
    if "burn" in condition:
        return [
            "Move the person away from the heat source.",
            "Cool the burn with clean running water for 10–20 minutes.",
            "Do NOT apply butter, oil, toothpaste, or ice.",
            "Cover loosely with a clean cloth.",
            "Seek medical help if the burn is large or deep."
        ]

    # Bleeding
    if "bleed" in condition:
        return [
            "Apply firm pressure using a clean cloth.",
            "Raise the injured area if possible.",
            "Do not remove objects stuck in the wound.",
            "Continue pressure until bleeding stops.",
            "Get medical help if bleeding is heavy."
        ]

    # Default
    return [
        "Ensure the area is safe before helping.",
        "Keep the person calm and still.",
        "Do not give food or medicine.",
        "Seek professional medical help as soon as possible."
    ]


# ---------------- UI ---------------- #
def show(low_bandwidth):
    st.header("🚑 Emergency Procedures")

    if low_bandwidth:
        emergency = st.selectbox(
            "Select emergency type",
            [
                "Bleeding",
                "Burns",
                "Choking",
                "CPR",
                "Unconscious",
                "🤖 AI First Aid (Smart)"
            ]
        )

        # ---------------- EXISTING STATIC CONTENT ---------------- #
        if emergency == "Bleeding":
            st.subheader("Bleeding Control")
            st.write("1. Apply direct pressure with clean cloth")
            st.write("2. Elevate injured area above heart if possible")
            st.write("3. Add more layers if bleeding soaks through")
            st.write("4. Use tourniquet ONLY for severe bleeding")
            st.warning("Seek medical help for serious wounds")

        elif emergency == "Burns":
            st.subheader("Burn Treatment")
            st.write("1. Cool with running water for 10-15 minutes")
            st.write("2. Remove jewelry/clothing near burn (unless stuck)")
            st.write("3. Cover with clean, non-stick dressing")
            st.write("4. Do NOT apply ice, butter, or ointments")
            st.warning(
                "Get medical help for:\n"
                "- Large burns\n"
                "- Face/hand/genital burns\n"
                "- Chemical/electrical burns"
            )

        elif emergency == "Choking":
            st.subheader("Choking Response")
            st.write("For conscious adults/children (>1 year):")
            st.write("1. Ask 'Are you choking?'")
            st.write("2. Perform 5 back blows")
            st.write("3. Do 5 abdominal thrusts")
            st.write("4. Repeat until object is out")
            st.error("Call emergency services if choking persists")

        elif emergency == "CPR":
            st.subheader("CPR Steps")
            st.write("1. Check responsiveness and breathing")
            st.write("2. Call for help")
            st.write("3. Push hard and fast (100–120/min)")
            st.write("4. 30 compressions + 2 breaths")
            st.info("Hands-only CPR is acceptable")

        elif emergency == "Unconscious":
            st.subheader("Unconscious Person")
            st.write("1. Check for danger")
            st.write("2. Check responsiveness")
            st.write("3. Check breathing")
            st.write("4. Recovery position if breathing")
            st.write("5. CPR if not breathing")
            st.error("Call emergency services immediately")

        # ---------------- AI FIRST AID ---------------- #
        elif emergency == "🤖 AI First Aid (Smart)":
            st.subheader("🤖 AI First Aid Generator")

            condition = st.text_input(
                "What happened?",
                placeholder="e.g., Snake bite in a farm"
            )

            age = st.selectbox(
                "Age group",
                ["Child", "Adult", "Elderly"]
            )

            setting = st.selectbox(
                "Current setting",
                ["Rural area", "No hospital nearby", "Outdoor / farm", "Home"]
            )

            if st.button("Generate First Aid Steps"):
                if not condition:
                    st.warning("Please describe the condition.")
                else:
                    steps = generate_ai_first_aid(condition, age, setting)
                    st.subheader("🩹 First Aid Steps")
                    for i, step in enumerate(steps, 1):
                        st.write(f"**Step {i}:** {step}")

                    st.warning(
                        "⚠️ This guidance is for first aid only. "
                        "Seek professional medical help as soon as possible."
                    )

    # ---------------- NORMAL BANDWIDTH MODE ---------------- #
    else:
        tab1, tab2 = st.tabs(["Bleeding", "Burns"])
        with tab1:
            st.subheader("Stop Bleeding")
            st.video("https://youtu.be/8pTaqY40-Rs?si=Aep-WObkRqCDizVS")
        with tab2:
            st.subheader("Burns")
            st.video("https://youtu.be/z_5tuB1YMK0?si=dm0V8-8I0gUgBzlZ")
