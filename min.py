from translate import Translator

def translate_text(text, source_lang, target_lang):
    translator = Translator(to_lang=target_lang, from_lang=source_lang)
    translation = translator.translate(text)
    return translation

def main():
    print("Welcome to the Chinese-English translation program")
    print("\nPlease select a translation direction:")
    print("1. Chinese to English Translation")
    print("2. English to Chinese Translation")
    print("3. Exit")
    while True:

        choice = input("Please Enter the Option（en/zh/exit）: ")

        if choice == "en":
            source_lang = "zh"
            target_lang = "en"
        elif choice == "zh":
            source_lang = "en"
            target_lang = "zh"
        elif choice == "exit":
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
