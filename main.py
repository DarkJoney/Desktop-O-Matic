import engine.analysis as analysis
import engine.datamove as datamove

def batchProcessorByType():
    desktopLoc = analysis.locate_desktop()
    targetTypes = datamove.parserLoader("data/msWord")
    fileType = targetTypes[0]
    fileType = fileType.strip('\n')
    targetTypes.pop(0)
    for i in targetTypes:
        targetFileType = i.strip('\n')
        locatedFiles = analysis.get_files(targetFileType, desktopLoc)
        if locatedFiles == []:
            pass
        else:
            datamove.move_to_folder_by_type(locatedFiles,targetFileType,fileType)

def main():
    print("hello!")
    desktopLoc = analysis.locate_desktop()
    #locatedFiles = analysis.get_files(".pdf", desktopLoc)
    #analysis.move_to_folder(locatedFiles, ".pdf")
    #analysis.move_to_folder_timeline(locatedFiles, ".pdf")
    print(analysis.checkIfCameraPresentInExif(r"C:\Users\darkj\Desktop\DSC08114-Enhanced copy.jpg"))
    print(analysis.checkIfCameraPresentInExif(r"C:\Users\darkj\Desktop\photo_2022-06-24_12-17-29.jpg"))
    #analysis.defineIfAudioIsMusic("01 Kallisto.m4a")
    datamove.parserLoader("data/msWord")
    batchProcessorByType()
if __name__ == '__main__':
    main()