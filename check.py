import google.generativeai
from dotenv import load_dotenv
import os
load_dotenv()

google.generativeai.configure(api_key=os.getenv("GOOGLE_GENERATIVE_AI_API_KEY"))
models = google.generativeai.list_models()
for model in models:
    print(model.name, model.supported_generation_methods)

    '''
        Examples:

        # 1. Retrieve student details
        User's Question: "Show me every student record."
        SQL Query Result:
        | NAME   | CLASS           | ROLL_NO | SECTION | MARKS |
        |--------|-----------------|---------|---------|-------|
        | Satyam | GenerativeAI    | 450     | A       | 100   |
        | Ananya | MachineLearning | 123     | A       | 92    |
        | Rohan  | DataScience     | 312     | B       | 85    |

        Response: "Here are the student records: Satyam in GenerativeAI (Roll No: 450, Section: A) with 100 marks; Ananya in MachineLearning (Roll No: 123, Section: A) with 92 marks; Rohan in DataScience (Roll No: 312, Section: B) with 85 marks."

        # 2. Students in Section A
        User's Question: "List the names and roll numbers of students in section A."
        SQL Query Result:
        | NAME   | ROLL_NO |
        |--------|---------|
        | Satyam | 450     |
        | Ananya | 123     |

        Response: "The students in Section A are Satyam (Roll No: 450) and Ananya (Roll No: 123)."

        # 4. Specific Student Details
        User's Question: "Give me all details for the student with roll number 312."
        SQL Query Result:
        | NAME  | CLASS       | ROLL_NO | SECTION | MARKS |
        |-------|-------------|---------|---------|-------|
        | Rohan | DataScience | 312     | B       | 85    |

        Response: "Student Rohan is enrolled in DataScience, Roll No: 312, Section: B, with 85 marks."

        # 5. Retrieve student details (open question)
        User's Question: "Show me every student record."
        SQL Query Result:
        | NAME   | CLASS           | ROLL_NO | SECTION | MARKS |
        |--------|-----------------|---------|---------|-------|
        | Satyam | GenerativeAI    | 450     | A       | 100   |
        | Ananya | MachineLearning | 123     | A       | 92    |
        | Rohan  | DataScience     | 312     | B       | 85    |

        Response: "Here are the student records: Satyam in GenerativeAI (Roll No: 450, Section: A) with 100 marks; Ananya in MachineLearning (Roll No: 123, Section: A) with 92 marks; Rohan in DataScience (Roll No: 312, Section: B) with 85 marks."

        # 6. Yes/No style query with a single record
        User's Question: "Anyone with GenerativeAI class?"
        SQL Query Result:
        | NAME   | CLASS        | ROLL_NO | SECTION | MARKS |
        |--------|--------------|---------|---------|-------|
        | Satyam | GenerativeAI | 450     | A       | 100   |

        Response: "Yes, Satyam is in GenerativeAI, Roll No: 450, Section: A, and has 100 marks."

        # 7. Counting records
        User's Question: "How many students are there in each class?"
        SQL Query Result:
        | CLASS           | student_count |
        |-----------------|---------------|
        | GenerativeAI    | 1             |
        | MachineLearning | 1             |
        | DataScience     | 1             |

        Response: "There is 1 student each in the following classes: GenerativeAI, MachineLearning, and DataScience."

        # 8. Non-existence check  
        User's Question: “Anyone in CloudComputing class?”  
        SQL Query Result: *(empty)*  

        Response:  
        “No, there are no students in CloudComputing.”

        # 9. Direct data request  
        User's Question: “List the names and roll numbers of students in section A.”  
        SQL Query Result:
        | NAME   | ROLL_NO |
        |--------|---------|
        | Satyam | 450     |
        | Ananya | 123     |

        Response:  
        “The students in Section A are Satyam (Roll No: 450) and Ananya (Roll No: 123).”

        # 10. Single-row detail  
        User's Question: “What are the details of Satyam?”  
        SQL Query Result:
        | NAME   | CLASS        | ROLL_NO | SECTION | MARKS |
        |--------|--------------|---------|---------|-------|
        | Satyam | GenerativeAI | 450     | A       | 100   |

        Response:  
        “Satyam is in GenerativeAI (Roll No: 450, Section: A) and has 100 marks.”

        # 11. Multi-row**  
        User's Question: “Students with more than 80 marks”  
        SQL Result:
        | NAME   | CLASS           | ROLL_NO | SECTION | MARKS |
        |--------|-----------------|---------|---------|-------|
        | Satyam | GenerativeAI    | 450     | A       | 100   |
        | Ananya | MachineLearning | 123     | A       | 92    |
        | Rohan  | DataScience     | 312     | B       | 85    |
        …  
        Response:
        | NAME   | CLASS           | ROLL_NO | SECTION | MARKS |
        |--------|-----------------|---------|---------|-------|
        | Satyam | GenerativeAI    | 450     | A       | 100   |
        | Ananya | MachineLearning | 123     | A       | 92    |
        | Rohan  | DataScience     | 312     | B       | 85    |
        | Vikram | CloudComputing  | 274     | C       | 88    |
        | Meera  | DevOps          | 831     | B       | 91    |
        | Nisha  | Robotics        | 957     | C       | 82    |
        | Karan  | IoT             | 618     | B       | 89    |
        | Sneha  | Blockchain      | 742     | A       | 95    |
        | Rhea   | NLP             | 294     | B       | 90    |
        | Tanvi  | ComputerVision  | 583     | A       | 84    |
        | Lina   | UX/UI           | 139     | B       | 87    |
        | Yash   | AR/VR           | 908     | A       | 93    |

    '''
    '''
        You are an assistant that converts English questions into SQL queries. The database is `student.db` and contains a single table:

        STUDENT(
        NAME       VARCHAR(25),
        CLASS      VARCHAR(25),
        ROLL_NO    INT PRIMARY KEY,
        SECTION    VARCHAR(25),
        MARKS      INT
        );

        When you receive a user request in plain English, output only the SQL query (no explanations). Use standard ANSI-SQL.

        Examples:

        # 1. Get all columns for every student
        English: “Show me every student record.”
        SQL:
        SELECT * FROM STUDENT;

        # 2. Find students in section A
        English: “List the names and roll numbers of students in section A.”
        SQL:
        SELECT NAME, ROLL_NO FROM STUDENT WHERE SECTION = 'A';

        # 3. Top scorers
        English: “Which students scored more than 90 marks?”
        SQL:
        SELECT NAME, MARKS FROM STUDENT WHERE MARKS > 90;

        # 4. Count by class
        English: “How many students are there in each class?”
        SQL:
        SELECT CLASS, COUNT(*) AS student_count FROM STUDENT GROUP BY CLASS;

        # 5. Specific student lookup
        English: “Give me all details for the student with roll number 312.”
        SQL:
        SELECT * FROM STUDENT WHERE ROLL_NO = 312;

        ---

        Now, translate the following English request into an SQL query:
    '''