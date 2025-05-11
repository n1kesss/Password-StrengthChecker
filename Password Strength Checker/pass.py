import streamlit as st #webapp
import re 
import random
import string
#regular expression, to find patterns of number or characters. eg. to check if there is captial letter in password

st.set_page_config(page_title="Password Strength Chcecker", page_icon="🔐") #page title

st.title("🔒 Password Strength Checker")
st.markdown("""
## Welcome to the Ultimate Password Roast!👋
Think your password is strong? Let’s find out before a toddler with WiFi cracks it.
            Drop your password below — we’ll judge it harder than your ex and toss in some spicy tips to beef it up.""")

#password text field
password = st.text_input("Enter your weak excuse for a password:", type="password")

feedback = []

score = 0


if password:
    if len(password) >= 8:
        score +=1
    else:
        feedback.append("❌ That’s cute. Now give us at least 8 characters, rookie.")
    
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append('❌ Caps lock stuck? Or just feeling lazy today?')
    
    #to check numbers from 0-9
    
    if re.search(r'[0-9]',password):
        score += 1
    else:
        feedback.append("❌ No digits? What is this, a bedtime story?")

    #or

    # if re.search(r'\d',password):
    #     score += 1
    # else:
    #     feedback.append("❌Password should be at least 8 characters long.")

    #to check characters

    if re.search(r'[!@#$%]',password):
        score += 1 
    else:
        feedback.append("❌ Your password is as bland as boiled rice. Throw in some @#$%!")

#check the strength
    if score == 4:
        feedback.append("✅ Now that’s strong. You might even remember it, too.")
    elif score == 3:
        feedback.append("🟡 Your password is medium — like lukewarm tea: not bad, not great, just meh.")
    else:
        feedback.append("❌ Is that your password, or did your keyboard just sneeze?")

    if feedback:
        st.markdown("## Improvement Suggestions")
        for tip in feedback:
            st.write(tip)
    



def generate_password(length):
    characters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()_-+="
    return "" .join(random.choice(characters) for i in range(length))


password_length = st.number_input("Enter the length of your password, and we’ll generate something better than your ‘masterpiece’ 🔥💻", min_value=8, max_value=20, value=8)
if st.button('Brace yourself'):
    password = generate_password(password_length)
    st.success(f'🔑 Here’s your new password: {password}')


