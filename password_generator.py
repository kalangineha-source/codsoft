"""
Password Generator Application
A beginner-friendly Python application to generate strong random passwords
with customizable complexity options.

Author: [Your Name]
Date: May 2026
Purpose: College Mini-Project
"""

# Import required modules
import random
import string
import pyperclip  # For clipboard functionality

# ============================================================================
# FUNCTION DEFINITIONS
# ============================================================================

def get_password_length():
    """
    Prompt the user to enter the desired password length.
    
    Returns:
        int: The desired password length (must be greater than 0)
    
    Raises:
        ValueError: If input is not a valid positive integer
    """
    while True:
        try:
            # Ask user for password length
            length = int(input("\n📝 Enter desired password length (minimum 4): "))
            
            # Validate that length is greater than 0
            if length <= 0:
                print(" Error: Password length must be greater than 0!")
                continue
            
            if length < 4:
                print("  Warning: Password should be at least 4 characters long for security.")
                confirm = input("Continue anyway? (yes/no): ").lower()
                if confirm != 'yes':
                    continue
            
            return length
        
        except ValueError:
            # Handle invalid input (non-integer values)
            print(" Error: Please enter a valid number!")


def get_complexity_options():
    """
    Prompt the user to choose password complexity options.
    
    Returns:
        dict: Dictionary containing selected character types
        Example: {'uppercase': True, 'lowercase': True, 'numbers': False, 'special': True}
    
    Raises:
        ValueError: If no character type is selected
    """
    options = {
        'uppercase': False,
        'lowercase': False,
        'numbers': False,
        'special': False
    }
    
    print("\n Select password complexity options:")
    print("-" * 40)
    
    # Ask for each character type
    try:
        uppercase_input = input("Include UPPERCASE letters? (yes/no): ").lower()
        options['uppercase'] = uppercase_input in ['yes', 'y', '1']
        
        lowercase_input = input("Include lowercase letters? (yes/no): ").lower()
        options['lowercase'] = lowercase_input in ['yes', 'y', '1']
        
        numbers_input = input("Include numbers? (yes/no): ").lower()
        options['numbers'] = numbers_input in ['yes', 'y', '1']
        
        special_input = input("Include special characters? (yes/no): ").lower()
        options['special'] = special_input in ['yes', 'y', '1']
        
        # Validate that at least one option is selected
        if not any(options.values()):
            print(" Error: At least one character type must be selected!")
            return get_complexity_options()  # Recursively ask again
        
        return options
    
    except KeyboardInterrupt:
        print("\n  Operation cancelled.")
        return None


def build_character_pool(options):
    """
    Build a pool of characters based on user's complexity selections.
    
    Args:
        options (dict): Dictionary with character type selections
    
    Returns:
        str: A string containing all selected character types combined
    
    Example:
        If user selects uppercase and numbers:
        Returns: "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    """
    character_pool = ""
    
    # Add uppercase letters if selected
    if options['uppercase']:
        character_pool += string.ascii_uppercase
    
    # Add lowercase letters if selected
    if options['lowercase']:
        character_pool += string.ascii_lowercase
    
    # Add numbers if selected
    if options['numbers']:
        character_pool += string.digits
    
    # Add special characters if selected
    if options['special']:
        # Common special characters that are safe to use
        character_pool += string.punctuation
    
    return character_pool


def generate_password(length, character_pool):
    """
    Generate a random password from the character pool.
    
    Args:
        length (int): The desired length of the password
        character_pool (str): String of characters to choose from
    
    Returns:
        str: A randomly generated password
    
    Logic:
        Uses random.choice() to select random characters from the pool
        and repeats the process 'length' times to create the password
    """
    # Generate password by randomly selecting characters from the pool
    password = ''.join(random.choice(character_pool) for _ in range(length))
    
    return password


def calculate_password_strength(length, options):
    """
    Calculate and return the strength level of the generated password.
    
    Args:
        length (int): The length of the password
        options (dict): Dictionary with selected character types
    
    Returns:
        str: Password strength level ("Weak", "Medium", or "Strong")
    
    Logic:
        - Weak: Short password (< 8 chars) OR few character types selected
        - Medium: Moderate length (8-12 chars) AND at least 2 types selected
        - Strong: Long password (> 12 chars) AND 3+ types selected
    """
    selected_types = sum(options.values())  # Count how many types are selected
    
    # Determine strength based on length and variety
    if length < 8 or selected_types < 2:
        return "Weak "
    elif length <= 12 and selected_types >= 2:
        return "Medium "
    else:
        return "Strong "


def display_password_info(password, options, strength):
    """
    Display the generated password and its information in a formatted way.
    
    Args:
        password (str): The generated password
        options (dict): Dictionary with selected character types
        strength (str): The password strength level
    """
    print("\n" + "=" * 50)
    print(" PASSWORD GENERATED SUCCESSFULLY!")
    print("=" * 50)
    
    # Display the password in a highlighted box
    print(f"\n Your Password: {password}")
    print(f"\n Password Details:")
    print(f"   • Length: {len(password)} characters")
    print(f"   • Strength: {strength}")
    
    # Show which character types are included
    print(f"\n Character Types Used:")
    if options['uppercase']:
        print(f"   ✓ Uppercase letters (A-Z)")
    if options['lowercase']:
        print(f"   ✓ Lowercase letters (a-z)")
    if options['numbers']:
        print(f"   ✓ Numbers (0-9)")
    if options['special']:
        print(f"   ✓ Special characters (!@#$%^&*...)")
    
    print("\n" + "=" * 50)


def copy_to_clipboard(password):
    """
    Copy the generated password to the system clipboard.
    
    Args:
        password (str): The password to copy
    
    Returns:
        bool: True if successful, False if failed
    """
    try:
        pyperclip.copy(password)
        print(" Password copied to clipboard!")
        return True
    except Exception as e:
        print(f"  Could not copy to clipboard: {e}")
        print(f"   You can manually copy this password: {password}")
        return False


def ask_user_action():
    """
    Ask the user what they want to do next.
    
    Returns:
        str: User's choice ('generate', 'copy', or 'exit')
    """
    while True:
        print("\nWhat would you like to do?")
        print("1. Generate another password")
        print("2. Copy this password to clipboard")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1/2/3): ").strip()
        
        if choice in ['1', '2', '3']:
            if choice == '1':
                return 'generate'
            elif choice == '2':
                return 'copy'
            else:
                return 'exit'
        else:
            print(" Invalid choice! Please enter 1, 2, or 3.")


# ============================================================================
# MAIN APPLICATION LOGIC
# ============================================================================

def main():
    """
    Main function to run the Password Generator Application.
    
    This function orchestrates the entire application flow:
    1. Display welcome message
    2. Get password length from user
    3. Get complexity options from user
    4. Generate password
    5. Display password and strength
    6. Allow user to copy or generate more passwords
    """
    
    # Display welcome message
    print("\n" + "=" * 50)
    print(" WELCOME TO PASSWORD GENERATOR ")
    print("=" * 50)
    print("Generate strong, random passwords with custom options!")
    print("=" * 50)
    
    # Main application loop - allows user to generate multiple passwords
    while True:
        try:
            # Step 1: Get password length from user
            password_length = get_password_length()
            
            # Step 2: Get complexity options from user
            complexity_options = get_complexity_options()
            
            # Handle if user cancelled
            if complexity_options is None:
                break
            
            # Step 3: Build character pool based on selected options
            char_pool = build_character_pool(complexity_options)
            
            # Step 4: Generate the password
            generated_password = generate_password(password_length, char_pool)
            
            # Step 5: Calculate password strength
            password_strength = calculate_password_strength(password_length, complexity_options)
            
            # Step 6: Display the generated password and its information
            display_password_info(generated_password, complexity_options, password_strength)
            
            # Step 7: Ask user what to do next
            while True:
                user_action = ask_user_action()
                
                if user_action == 'generate':
                    # Go back to main loop to generate another password
                    break
                
                elif user_action == 'copy':
                    # Copy password to clipboard
                    copy_to_clipboard(generated_password)
                    # Ask again what they want to do
                    continue
                
                elif user_action == 'exit':
                    # Exit the application
                    print("\nThank you for using Password Generator!")
                    print("Stay safe and remember to store passwords securely! \n")
                    return
        
        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\n\n Application interrupted. Goodbye!")
            break
        
        except Exception as e:
            # Catch any unexpected errors
            print(f"\n An unexpected error occurred: {e}")
            print("Please try again or restart the application.")


# ============================================================================
# PROGRAM ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    """
    This ensures that main() only runs when the script is executed directly,
    not when it's imported as a module in another script.
    """
    main()
