from auth import authenticate

def welcome():
    print('Welcome to BPM!')

    print('Have you been here before?')
    print('0:\tyes')
    print('1:\tno')
    user_type = input()
    
    if (user_type == '0'):
        print('Do you have a Spotify account?')
        print('0:\tyes')
        print('1:\tno')
        has_account = input()
        
        if (has_account == '0'):
            print('Login: ')
            authenticate()
        
        else:
            print('Please sign up for a Spotify account and return.\n')
    
