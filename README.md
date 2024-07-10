# scoreme-hackathon
# Objective:
The goal of this project was to extract tables from 'test3.pdf', a PDF file with irregular table formatting that made traditional extraction methods challenging.

Approach:
To handle the PDF's complexities, I utilized the pdfplumber library for text extraction. Initially, I split the PDF text into lines and processed each line to build complete transaction entries. It was clear that the transction table was to be started after the line, "statement of transactions".

Data Extraction Strategy:
Each row of the transction was divided into 2 lines which made it difficult to extract the table. But on further observing, I found that each transaction ended with the keyword "Dr". So I ran the script to consider same row untill Dr is observerd, which marked the end of a transactional entry. However, I encountered issues where transaction amounts and balances appeared in the same column probably because they were placed in different line. To resolve this, I developed an additional script to split these entries into separate columns for "Amount" and "Balance Remaining".

Excel Output:
The extracted data was  organized into an Excel workbook using the openpyxl library. Each transaction was structured with headers: "Date", "Transaction Info", "Amount", and "Balance Remaining". This organization facilitated easy analysis and further processing of financial records.

Conclusion:
In conclusion, the approach effectively addressed the challenges posed by the irregular table formatting in 'test3.pdf' using pdfplumber and openpyxl. By iterating through different scripts, I successfully segmented transaction data into meaningful columns. This method not only solved immediate extraction issues but also showcased scalability for handling diverse PDF layouts in future projects. Future improvements could focus on enhancing the accuracy and robustness of the extraction process to ensure reliable data extraction from a wider range of PDF formats.
