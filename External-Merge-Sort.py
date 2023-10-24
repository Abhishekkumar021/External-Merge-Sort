import random
import string

dataSize = int(input("\nEnter your size of dataSet :-   "))
with open("DataSet.txt", "w") as dataSet:
    for data in range(1, dataSize + 1):
        dataSet.write(
            str(data)
            + ","
            + "".join(random.choices(string.ascii_letters, k=3))
            + ","
            + str(random.randint(1, 999))
            + "\n"
        )
blockSize = int(input("\nEnter your block size :-   "))

Memory = int(input("\nEnter your Main Memory Size :-   "))


def filesCreated(data):
    if data % blockSize:
        return int(data / blockSize) + 1
    else:
        return int(data / blockSize)


print("\n***** Running *******\n")

fileCreating = filesCreated(dataSize)
fileCnt = 0
with open("dataSet.txt", "r") as datafile:
    for i in range(1, fileCreating + 1):
        with open(str(i) + ".txt", "w") as newFile:
            for line in range(blockSize):
                dataFile = datafile.readline()
                newFile.write(dataFile)
            if i != fileCreating:
                newFile.write(str(i + 1) + ".txt")
            else:
                newFile.write("NULL")
        fileCnt += 1
    datafile.close()


# print(fileCnt ,'&&', fileCreating)


def merge(listForSorting, l, mid, r):
    size1 = mid - l + 1
    size2 = r - mid

    # create temp lists
    a = [0] * (size1)
    b = [0] * (size2)

    # Copy data to temp lists a[] and b[]
    for i in range(0, size1):
        a[i] = listForSorting[l + i]

    for j in range(0, size2):
        b[j] = listForSorting[mid + 1 + j]

    # Merge the temp lists back into listForSorting[l..r]
    i = 0  # Initial index of first sub-list
    j = 0  # Initial index of second su-blist
    k = l  # Initial index of merged su-blist

    while i < size1 and j < size2:
        if int(a[i].split(",")[2]) <= int(b[j].split(",")[2]):
            listForSorting[k] = a[i]
            i += 1
        else:
            listForSorting[k] = b[j]
            j += 1
        k += 1

    # Copy the remaining elements of a[], if data remain in a[]
    while i < size1:
        listForSorting[k] = a[i]
        i += 1
        k += 1

    # Copy the remaining elements of b[], if data remain in b[]
    while j < size2:
        listForSorting[k] = b[j]
        j += 1
        k += 1
    return listForSorting


# l is for left index and r is right index of the
# sub-list of listForSorting to be sorted


def mergeSort(file, l, r):
    if len(file) == 1:
        return file

    if l < r:
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        mid = l + (r - l) // 2

        # Sort first and second halves
        mergeSort(file, l, mid)
        mergeSort(file, mid + 1, r)
        return merge(file, l, mid, r)


print("\n.......Run file generating .........")
for file in range(1, fileCreating + 1):
    dataFile = []
    with open(str(file) + ".txt", "r") as blockdata:
        txt = blockdata.read()
        txt = txt.split()
        txt = txt[:-1]
        dataFile.extend(
            txt
        )  # Extend function breaks in it's element and insert it in list
        with open("Run" + str(file) + ".txt", "w") as opt:
            dataFile = mergeSort(
                dataFile, 0, len(dataFile) - 1
            )  # memory-1 files sorting using merge Sort algorithm
            for line in range(len(dataFile)):
                opt.write(
                    dataFile[line] + "\n"
                )  # writing sorted data by iterating list

            if file != fileCreating:  # writing it's next file name at last line of file
                opt.write("Run" + str(file + 1) + ".txt")
            else:
                opt.write("NULL")
    dataFile.clear()
print("\n.......Run file generation Completed .........")


# Function for knowing how many files will create in any pass
def filesWillCreate(previousFiles):
    if previousFiles % (Memory - 1):
        return (previousFiles // (Memory - 1)) + 1
    else:
        return previousFiles // (Memory - 1)


# fileCreating is an integer type varible which contained how many run files are there

newFiles = filesWillCreate(fileCreating)
newfileCnt = 1
print(f"\n.......Merge Sort Pass 1 file Creating .........\n")

for sortFile in range(1, newFiles + 1):
    dataFile = []
    for mem in range(1, Memory):
        if newfileCnt > fileCnt:
            break
        with open("Run" + str(newfileCnt) + ".txt", "r") as runfile:
            txt = runfile.read()
            txt = txt.split()  # When set to None (the default value), will split on
            # any whitespace character (including \n \r \t \f and spaces)
            #  and will discard empty strings from the result.
            txt = txt[:-1]
            dataFile.extend(txt)
            newfileCnt += 1
            runfile.close()

    dataFile = mergeSort(dataFile, 0, (len(dataFile) - 1))

    with open("Pass1" + "_" + str(sortFile) + ".txt", "w") as newFile:
        for i in range(len(dataFile)):
            newFile.write(dataFile[i] + "\n")
        if sortFile != newFiles:  # writing it's next file name at last line of file
            newFile.write("Pass1" + "_" + str(sortFile) + ".txt")
        else:
            newFile.write("NULL")

        newFile.close()
    dataFile.clear()
print(f"\n.......Merge Sort Pass 1 file Creation Completed  .........\n")


PrevPassFiles = newFiles
newFiles = filesWillCreate(PrevPassFiles)
passCount = 1
isTrue = 1
while newFiles > 0:
    idx = 1
    for files in range(1, newFiles + 1):
        dataFile = []
        for mem in range(1, Memory):
            if (
                idx > PrevPassFiles
            ):  # condition to acess those files only whoever created in previous pass
                break
            with open(
                "Pass" + str(passCount) + "_" + str(idx) + ".txt", "r"
            ) as mergingFile:
                txt = mergingFile.read()
                txt = txt.split()
                txt = txt[:-1]  # removing last line which contain next file name
                dataFile.extend(txt)
                idx += 1
        dataFile = mergeSort(dataFile, 0, (len(dataFile) - 1))

        if (
            newFiles == 1
        ):  # tracking if we reach in last pass then there will generate one file after combining two files and it would be output file
            print(f"\n.......Final OutputFile Creating .........\n")
            with open("FinalSortedOutput.txt", "w") as opt:
                for i in range(len(dataFile)):
                    opt.write(dataFile[i] + "\n")
                print(f"\n.......Final OutputFile Created .........\n")
            newFiles = 0
            isTrue = 0
            break

        else:
            with open(
                "Pass" + str(passCount + 1) + "_" + str(files) + ".txt", "w"
            ) as opt:
                for i in range(len(dataFile)):
                    opt.write(dataFile[i] + "\n")
                if files != newFiles:
                    opt.write(
                        "Pass" + str(passCount + 1) + "_" + str(files + 1) + ".txt"
                    )

                else:
                    opt.write("NULL")
    if isTrue:
        print(f"\n....... Generating pass {passCount+1} file .........\n")
    passCount += 1  # increamenting pass count
    PrevPassFiles = newFiles
    newFiles = filesWillCreate(
        PrevPassFiles
    )  # calculating how many files will create in this pass and it will help to stoping the while loop

print("\n***** Completed *******\n")
