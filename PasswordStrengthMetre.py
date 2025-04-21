import streamlit as st
import string
import random

# Common weak passwords to reject
blacklist = ["password", "123456", "qwerty", "password123", "admin", "letmein"]

def check_password_strength(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Make your password at least 8 characters long.")

    if any(char.isupper() for char in password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter.")

    if any(char.islower() for char in password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter.")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        suggestions.append("Include at least one number (0–9).")

    special_chars = "!@#$%^&*"
    if any(char in special_chars for char in password):
        score += 1
    else:
        suggestions.append(f"Include at least one special character ({special_chars}).")

    return score, suggestions

def generate_strong_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(12))

def main():
    st.title("🔐 Password Strength Checker")

    password = st.text_input("Enter your password:", type="password")

    if password:
        if password.lower() in blacklist:
            st.error("❌ This is a common weak password. Please choose a different one.")
        else:
            score, feedback = check_password_strength(password)

            st.subheader("🔍 Password Analysis")
            if score <= 2:
                st.error("🔴 Strength: Weak")
                for item in feedback:
                    st.write("👉", item)
                st.info("✨ Suggested Strong Password: `" + generate_strong_password() + "`")
            elif score <= 4:
                st.warning("🟡 Strength: Moderate")
                for item in feedback:
                    st.write("💡", item)
                st.info("✨ Suggested Strong Password: `" + generate_strong_password() + "`")
            else:
                st.success("🟢 Strength: Strong")
                st.balloons()
                st.write("✅ Your password is secure!")

if __name__ == "__main__":
    main()
