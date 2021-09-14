for root, dirs, files in os.walk(os.path.abspath("Images/")):
    for file in files:
        image_path = os.path.join(root, file)
        print(image_path)