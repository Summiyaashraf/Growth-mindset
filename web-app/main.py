import streamlit as st
import random

# Motivational Quotes
quotes = [
    "🌟 Your brain is like a muscle. The more you use it, the stronger it gets.",
    "💪 Mistakes are proof that you are trying.",
    "🚀 Failure is the opportunity to begin again more intelligently.",
    "🔥 Growth starts at the end of your comfort zone.",
]

# App Title
st.title("🌱 Growth Mindset Challenge")
st.subheader("Unlock your potential with a positive mindset! 🚀")

# User Input for Name
user_name = st.text_input("👤 Enter your name:")

if user_name:
    st.write(f"Hey {user_name}, keep pushing forward! 🚀")

# Show Motivational Quote
if st.button("💡 Get Inspired!"):
    st.success(random.choice(quotes))

# Quiz Section
st.subheader("🤔 Quick Growth Mindset Quiz")
question = "What should you do when you face failure?"
options = [
    "😢 Give up and stop trying",
    "🚀 Learn from mistakes and try again",
    "😠 Blame others for the failure",
]
answer = st.radio("Choose the correct answer:", options)

if st.button("Check Answer"):
    if answer == options[1]:
        st.success("✅ Correct! Growth mindset is about learning and improving. 🎉")
    else:
        st.error("❌ Oops! Try again. Growth mindset is about learning and improving.")

# Daily Reflection
st.subheader("📅 Track Your Daily Growth Mindset Progress")
daily_log = st.text_area("Write about what you learned today:")

if st.button("Save Progress"):
    st.success("🎯 Great! Keep pushing forward!")

st.write("💪 Remember: Growth is a journey, not a destination. Keep striving to be better! 🚀")
