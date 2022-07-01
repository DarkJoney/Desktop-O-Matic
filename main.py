import engine.analysis as analysis

def main():
    print("hello!")
    desktopLoc = analysis.locate_desktop()
    locatedFiles = analysis.get_files(".pdf", desktopLoc)
    #analysis.move_to_folder(locatedFiles, ".pdf")
    analysis.move_to_folder_timeline(locatedFiles, ".pdf")

if __name__ == '__main__':
    main()