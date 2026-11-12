
import string

print("=" * 40)
print("       PASSWORD STRENGTH CHECKER")
print("=" * 40)

password = input("Enter a sample password: ")

score = 0
feedback = []

# 1. Check password length
if len(password) >= 8:
    score += 1
    print("[PASS] Minimum length satisfied")
else:
    feedback.append("Use at least 8 characters.")
    print("[FAIL] Password must contain at least 8 characters.")

# 2. Check uppercase letters
if any(char.isupper() for char in password):
    score += 1
    print("[PASS] Uppercase letter present")
else:
    feedback.append("Add at least one uppercase letter (A-Z).")
    print("[FAIL] No uppercase letter found.")

# 3. Check lowercase letters
if any(char.islower() for char in password):
    score += 1
    print("[PASS] Lowercase letter present")
else:
    feedback.append("Add at least one lowercase letter (a-z).")
    print("[FAIL] No lowercase letter found.")

# 4. Check numbers
if any(char.isdigit() for char in password):
    score += 1
    print("[PASS] Number present")
else:
    feedback.append("Include at least one number (0-9).")
    print("[FAIL] No number found.")

# 5. Check special characters
if any(char in string.punctuation for char in password):
    score += 1
    print("[PASS] Special character present")
else:
    feedback.append("Include a special character (@, #, $, etc.).")
    print("[FAIL] No special character found.")

# Classify password strength
print("\n" + "=" * 40)

if score == 5 and len(password) >= 12:
    print("PASSWORD STRENGTH: STRONG")
elif score >= 3:
    print("PASSWORD STRENGTH: MEDIUM")
else:
    print("PASSWORD STRENGTH: WEAK")

print("Score:", score, "/ 5")

# Display suggestions
print("\nSECURITY FEEDBACK:")

if len(password) < 12:
    print("- Consider using at least 12 characters.")

if feedback:
    for suggestion in feedback:
        print("-", suggestion)
else:
    print("All five basic security checks passed!")

print("\nThank you for using Password Strength Checker!")
print("=" * 40)
