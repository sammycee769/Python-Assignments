menu = """
        List of Menu functions
        1. Phone Book
        2. Messages
        3. Chat
        4. Call register
        5. Tones
        6. Settings
        7. Call divert
        8. Games
        9. Calculator
        10.Reminder
        11.Clock
        12.Profiles
        13.Sim services
        0. Exit
                    """
phone_book_options = """
        1. Search
        2. Service Nos
        3. Add name
        4. Erase
        5. Edit
        6. Assign Tone
        7. Send b'card
        8. Options
        9. Speed dials
        10.Voice tags
        0. Back
                  """
messages_options = """
        1.Write messages
        2.Inbox
        3.Outbox
        4.Picture messages
        5.Templates
        6.Smileys
        7.Message settings
        8.Info service
        9.Voice service
        10.Service command editor
        0. Back
        """
call_register_options ="""
        1.Missed calls 
        2.Received calls
        3.Dialled numbers
        4.Erase recent call lists
        5.Show call duration
        6.Show call costs
        7.Call costs settings
        8.Prepaid credit
        0. Back
            """
call_duration_options = """
            1.Last call duration
            2.All calls' duration
            3.Received calls' duration
            4.Dialled calls' duration
            5.Clear timers
            0. Back
            """
call_costs_options = """
            1.Last call cost
            2.All calls' cost
            3.Clear counters
            0. Back
            """
call_settings_options = """
            1.Call cost limit
            2.Show costs in
            0. Back
            """
tones_options ="""
            1.Ringing tone
            2.Ringing volume
            3.Incoming call alert
            4.Composer
            5.Messae alert tone
            6.Keypad tones
            7.Warning and game tones
            8.Vibrating alert
            9.Screen saver
            0. Back
            """
settings_options = """
            1.Call Settings
            2.Phone settings
            3.Security settings
            4.Restore factory settings
            0.Back
            """
phonecall_settings_options = """
                1.Automatic redial
                2.Speed dialing
                3.Call waiting
                4.Own number sending
                5.Phone line in use
                6.Automatic answer 
                0.Back
                """
phone_settings_options = """
                1. Language
                2. Cell info display
                3. Welcome note
                4. Network selection
                5. Lights2
                6. Confirm SIM service actions
                0. Back
                """
security_settings_options = """
                1. PIN code request
                2. Call barring service
                3. Fixed dialling
                4. Closed user group
                5. Phone security
                6. Change access codes  
                0. Back
                """
clock_options = """
            1.Alarm clock
            2.Clock settings
            3.Date settings
            4.Stopwatch
            5.Countdown timer
            6.Auto update of date and time
            0.Back
            """


print(menu)
while(True):
    menu_option = int(input("Enter an option: "))
    match menu_option:
        case 1:
            print("""
        1. Search
        2. Service Nos
        3. Add name
        4. Erase
        5. Edit
        6. Assign Tone
        7. Send b'card
        8. Options
        9. Speed dials
        10.Voice tags
        0. Back
                  """)
            options = int(input("Enter an option: "))
            match options:
                case 8:
                    print("""
                    1.Type of view
                    2.Memory status
                    0.Back
                    """)
                    back_option = int(input("Enter an option: "))
                    match back_option:
                        case 0:
                            print(phone_book_options)
                        case _:
                            print("Enter A valid Option")

                case 0:
                    print(menu)
                case _:
                    print("Enter A valid Option")
        case 2:
            while (True):
                print(messages_options)
                message_input = int(input("Enter an option: "))
                match message_input:
                    case 7:
                        while(True): 
                            print("""
                            1.Set 1
                            2.Common
                            0.Back""")
                            back_message = int(input("Enter an option: "))
                            match back_message :
                                case 0:
    #                                print(messages_options)
                                    break
                                case _:
                                    print("Enter A valid Option")
                    case 0:
                        print(menu)
                        break
                    case _:
                        print("Enter A valid Option")
        case 4.:
            while(True):
                print(call_register_options)
                call_register_input = int(input("Enter an option: "))
                match call_register_input:
                    case 5:
                        while(True):
                            print(call_duration_options)
                            call_duration_input = int(input("Enter an option: "))
                            match call_duration_input:
                                 case 0:
                                    break
                                 case _:
                                    print("Enter A valid Option")
                    case 6:
                         while(True):
                            print(call_costs_options)
                            call_costs_input = int(input("Enter an option: "))
                            match call_costs_input:
                                 case 0:
                                    break
                                 case _:
                                    print("Enter A valid Option")
                    case 7:
                         while(True):
                            print(call_settings_options)
                            call_settings_input = int(input("Enter an option: "))
                            match call_settings_input:
                                 case 0:
                                    break
                                 case _:
                                    print("Enter A valid Option")
                    case 0:
                        print(menu)
                        break
                    case _:
                        print("Enter A valid Option")
        case 5:
            while(True):
                print(tones_options)
                tones_input = int(input("Enter an option: "))
                match tones_input:
                    case 0:
                        print(menu)
                        break
                    case _:
                        print("Enter A valid Option")
        case 6:
            while(True):
                print(settings_options)
                settings_input = int(input("Enter an option: "))
                match settings_input:
                    case 1:
                        while(True):
                            print(phonecall_settings_options)
                            phonecall_settings_input = int(input("Enter an option: "))
                            match phonecall_settings_input:
                                 case 0:
                                    break
                                 case _:
                                    print("Enter A valid Option")
                    case 2:
                         while(True):
                            print(phone_settings_options)
                            phone_settings_input = int(input("Enter an option: "))
                            match phone_settings_input:
                                 case 0:
                                    break
                                 case _:
                                    print("Enter A valid Option")
                    case 3:
                         while(True):
                            print(security_settings_options)
                            security_settings_input = int(input("Enter an option: "))
                            match security_settings_input:
                                 case 0:
                                    break
                                 case _:
                                    print("Enter A valid Option")
                    case 0:
                        print(menu)
                        break
                    case _:
                        print("Enter A valid Option")
        case 11:
            while(True):
                print(clock_options)
                clock_input = int(input("Enter an option: "))
                match clock_input:
                    case 0:
                        print(menu)
                        break
                    case _:
                        print("Enter A valid Option")
        case 0:
            print("Exiting.........")
            break
        case _:
            print("Enter A valid Option")


