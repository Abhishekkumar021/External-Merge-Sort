# External-Merge-Sort

External merge sort is a sorting algorithm designed to handle very large datasets that cannot fit entirely into the computer's main memory (RAM).
It's an efficient method for sorting massive amounts of data by using external storage, such as hard drives or SSDs, as an extension of the computer's memory.
External merge sort is commonly used in scenarios where the dataset is too large to be sorted entirely in memory.

# Steps to Sort the Large DataSet using External Sort

When dealing with extremely large datasets that exceed the available RAM, traditional in-memory sorting algorithms are not practical.
External merge sort addresses this issue by dividing the dataset into smaller blocks that fit in memory, sorting these blocks, and then merging them to produce a sorted result.

* Dividing Data into Blocks : The first step in external merge sort is to divide the large dataset into smaller blocks or chunks that can be loaded into memory. These blocks are usually a fixed size and are read from and written to external storage, such as a hard drive.

* Sorting in Memory : Each block of data is loaded into memory, and an in-memory sorting algorithm, like merge sort or quicksort, is applied to sort the data within each block. Sorting in-memory allows for efficient sorting operations.

* Merging Blocks : After sorting the individual blocks, they are merged together to create larger sorted sublists. This is done iteratively, combining two or more sublists at a time until the entire dataset is sorted.

* Multiple Passes : In cases where the dataset is too large to be sorted in a single pass, multiple passes are performed. The output of each pass becomes the input for the next pass. The number of passes required depends on the size of the dataset and the available memory.

* Final Merge : The final pass results in a single, fully sorted dataset. This is often written to a separate output file or location.
