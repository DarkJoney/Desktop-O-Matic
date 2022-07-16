import engine.analysis as analysis
import engine.datamove as datamove

def main():
    print("hello!")
    #desktopLoc = analysis.locate_desktop()
    #locatedFiles = analysis.get_files(".pdf", desktopLoc)
    #analysis.move_to_folder(locatedFiles, ".pdf")
    #analysis.move_to_folder_timeline(locatedFiles, ".pdf")
    print(analysis.checkIfCameraPresentInExif(r"C:\Users\darkj\Desktop\DSC08114-Enhanced copy.jpg"))
    print(analysis.checkIfCameraPresentInExif(r"C:\Users\darkj\Desktop\photo_2022-06-24_12-17-29.jpg"))
if __name__ == '__main__':
    main()