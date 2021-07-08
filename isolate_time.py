# -*- coding: utf-8 -*-
"""isolate_time

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qE1UjAKo6n2ZhY8X491aY3C9oYa_Srkb
"""

"""
Isolates timeframe selected by user using trial numbers and messages
Inputs: 
  - file_clean: cleaned file
  - directory: directory to save the file to
  - patientNum: patient number
  - inputMessage_Start: the user's input of which message to start from
  - inputMessage_End: the user's input of which message to end
  - msgStatements: full list of messages
  - msgTimes: full list of message time stamps
"""
def isolateTime(file_clean, directory, patientNum, inputMessage_Start, \
                inputMessage_End, msgStatements, msgTimes):
  range1 = [i for i in range(0,7)]
  file_read = pd.read_table(file_clean, usecols = range1, sep='\t',\
                            delim_whitespace=True, dtype = {"TIMESTAMP":int, \
                            "RIGHT_EYE_X":object, "RIGHT_EYE_Y":object, \
                            "RIGHT_PUPIL_SIZE":object, "LEFT_EYE_X":object, \
                            "LEFT_EYE_Y":object, "LEFT_EYE_PUPIL":object}, \
                            low_memory=False)
  rowCount = len(msgStatements)
  currRow = 0
  numFound = 0
  msgStatements = pd.DataFrame(msgStatements)
  msgTimes = pd.DataFrame(msgTimes)
  listFiles=list()
  while currRow < rowCount: 
    if inputMessage_Start in str(msgStatements.iloc[currRow,0]):
      startRow = currRow
      timeStart = msgTimes.iloc[startRow]
      ind_start = list(file_read.iloc[:,0]).index(int(timeStart))
      currRow = currRow + 1
      while currRow< rowCount:
        if inputMessage_Start in str(msgStatements.iloc[currRow, 0]):
          endRow = currRow
          timeEnd = msgTimes.iloc[endRow]
          ind_end = list(file_read.iloc[:,0]).index(int(timeEnd))
          numFound = numFound + 1
          saveFile = file_read.iloc[ind_start:ind_end]
          sFileOut = directory+'NLS_'+str(patientNum)+inputMessage_Start+str(numFound)+'.txt.gz'
          #print(sFileOut)
          np.savetxt(sFileOut, saveFile, delimiter=',', fmt='%s')
          listFiles.append(str(sFileOut))
          break
        else:
          currRow= currRow + 1
    else: 
      currRow = currRow + 1
    
  return listFiles