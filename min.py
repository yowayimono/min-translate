from translate import Translator

def translate_text(text, source_lang, target_lang):
    translator = Translator(to_lang=target_lang, from_lang=source_lang)
    translation = translator.translate(text)
    return translation

def main():
    print("Welcome to the Chinese-English translation program")
    while True:
        print("\nPlease select a translation direction:")
        print("1. Chinese to English Translation")
        print("2. English to Chinese Translation")
        print("3. Exit")
        choice = input("Please Enter the Option（1/2/3）: ")

        if choice == "1":
            source_lang = "zh"
            target_lang = "en"
        elif choice == "2":
            source_lang = "en"
            target_lang = "zh"
        elif choice == "3":
            print("Thank you for using, goodbye!")
            break
        else:
            print("Invalid option, please re-enter.")
            continue

        text = input("Please enter text to translate: \n")
        translation = translate_text(text, source_lang, target_lang)
        # print("\n原文:\n")
        
        print("\n------------------------------------------------------------------------------------------\n")
        print(text)
        print(translation)
        print("\n------------------------------------------------------------------------------------------\n")
if __name__ == "__main__":
    main()
