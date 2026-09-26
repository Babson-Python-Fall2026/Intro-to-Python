"""
OIM3600 — Weekly Exercise 1
Python Foundations

READ FIRST
----------
Complete this file. Do not create a separate Python solution file.

Each question is inside a function only to keep the questions separate.
You are NOT being tested on writing functions yet.

For predictions and written answers:
    - Write your answers as Python comments.
    - Make predictions BEFORE running the code.
    - If a prediction is wrong, DO NOT ERASE IT.
      Add the actual result and explain what you misunderstood.

For code:
    - Add code only where instructed.
    - Do not remove instructor headings or starter code unless told to.
    - At the bottom of the file, uncomment ONE question at a time and run it.

AI:
    - You may use your OIM3600 Project AI as a Python syntax/reference tool.
    - Do not ask AI to design or solve the question for you.
    - Submit the complete OIM3600 Project conversation(s) you used in ai_chat.txt.
"""


# ============================================================
# PART A — PREDICT BEFORE YOU RUN
# ============================================================


def question_a1():
    """
    A1 — Types and operations

    1. Predict all four outputs BEFORE running the code.
    2. Run it.
    3. If anything surprised you, explain why.
    """

    # PREDICTION:
    # 1. 73
    # 2. 777
    # 3. string
    # 4. integer

    x = "7"
    y = 3

    print(x + str(y))
    print(x * y)
    print(type(x))
    print(type(y))

    # ACTUAL RESULT:
    # 73
    # 777
    # <class 'str'>
    # <class 'int'>


    # EXPLANATION:
    #

#question_a1()
def question_a2():
    """
    A2 — Strings, indexing, and slicing

    1. Predict each output BEFORE running the code.
    2. Which expression creates the largest new string?
    3. Explain the difference between indexing and slicing in one sentence.
    """

    # PREDICTION:
    # 1. B
    # 2. e
    # 3. abson
    # 4. Babson
    # 5. egelloC nosbaB

    text = "Babson College"

    print(text[0])
    print(text[-1])
    print(text[1:6])
    print(text[:6])
    print(text[::-1])

    # ACTUAL RESULT:
    # 1. B
    # 2. e
    # 3. abson
    # 4. Babson
    # 5. egelloC nosbaB

    # Which expression creates the largest new string?
    # print(text[::-1])

    # Explain indexing vs slicing:
    # indexing gets a single element at one position  slicing creates a new object substring

#question_a2()
def question_a3():
    """
    A3 — Lists and sorting

    1. Predict both outputs BEFORE running the code.
    2. Does sorted(numbers) change numbers? Explain.
    """

    # PREDICTION:
    # numbers: [4, 1, 3, 2]
    # ordered: [1, 2, 3, 4]

    numbers = [4, 1, 3, 2]
    ordered = sorted(numbers)

    print(numbers)
    print(ordered)

    # ACTUAL RESULT:
    # numbers: [4, 1, 3, 2]
    # ordered: [1, 2, 3, 4]#

    # Does sorted(numbers) change numbers? Explain:
    # no, it returns a new sorted list

#question_a3()
# ============================================================
# PART B — INVESTIGATE A BUG
# ============================================================


def question_b1():
    """
    B1 — Why did the list disappear?

    1. Predict what the starter code will print.
    2. Run it.
    3. Use type() in a small experiment to investigate what happened.
    4. Rewrite the code so items becomes [1, 2, 3].
    5. Write a second correct version that leaves items unchanged and
       stores the sorted result in a new variable.
    """

    # PREDICTION:
    # None

    items = [3, 1, 2]
    items = items.sort()
    print(items)

    # ACTUAL RESULT:
    # None

    # INVESTIGATION:
    # Add a small experiment using type() below.
    # Keep your experiment in the file as evidence of your reasoning.
    print(type(items)) # prints <class 'NoneType'>


    # EXPLANATION:
    # Why did items become what it became?
    # because sort is a method that mutates list and returns None


    # FIX 1:
    # Rewrite the idea so items itself becomes [1, 2, 3].
    # YOUR CODE:
    items = [3, 1, 2]
    items.sort()
    print(items)



    # FIX 2:
    # Start with a fresh list.
    # Leave that original list unchanged and store the sorted
    # result in a different variable.
    # YOUR CODE:
    items = [3, 1, 2]
    new_items = sorted(items)
    print(items, new_items)


#question_b1()
# ============================================================
# PART C — MODIFY EXISTING DATA
# ============================================================


def question_c1():
    """
    C1 — Sales list

    Requirements:
    1. Create ordered_sales from largest to smallest.
    2. Leave sales unchanged.
    3. Create top_three containing the three largest sales.
    4. Create sale_count containing the number of sales.
    5. Print ordered_sales, top_three, and sale_count clearly using f-strings.

    Then answer the three questions below in comments.
    """

    sales = [1240.50, 875.25, 1920.00, 650.75, 1435.50, 990.00]

    # YOUR CODE:
    ordered_sales = sorted(sales, reverse = True)
    print(ordered_sales)
    print(sales)

    top_three = ordered_sales[:3]
    print(top_three)

    sale_count = len(sales)
    print(sale_count)

    print(f"Ordered Sales: {ordered_sales}")
    print(f"Top three: {top_three}")
    print(f"Sale Count: {sale_count}")


    # 6. Why does your code not change sales?
    # sorted() is a function that returns a new object, retrieves sales but does not mutate it


    # 7. Which line creates a new list by sorting?
    # ordered_sales = sorted(sales, reverse = True)


    # 8. Which line creates a new list by slicing?
    # top_three = ordered_sales[:3]

#question_c1()
# ============================================================
# PART D — BUILD A SMALL SALES SNAPSHOT
# ============================================================


def question_d1():
    """
    D1 — Build a small sales snapshot

    Starter data is below.

    Your program must:
    1. Remove the extra spaces from report_name.
    2. Display the report name in uppercase.
    3. Create a new descending sorted list without changing sales.
    4. Use indexing to obtain the largest and smallest sale.
    5. Use slicing to obtain the top three.
    6. Use len() for the number of sales.
    7. Use f-strings for the printed report.
    8. Add one additional useful line of information of your own choosing.

    Do NOT use a loop.
    Use only material from Workbook 2, Sections 1–6.

    Desired output should look similar to:

    SEPTEMBER SALES — Boston
    Number of sales: 6
    Largest sale: $1,920.00
    Smallest sale: $650.75
    Top three: [1920.0, 1435.5, 1240.5]
    """

    report_name = "  september sales  "
    region = "Boston"
    sales = [1240.50, 875.25, 1920.00, 650.75, 1435.50, 990.00]

    # YOUR CODE:
    '''
    1. Remove the extra spaces from report_name.
    '''
    report_name = report_name.strip()
    print(report_name)

    '''
        2. Display the report name in uppercase.
    '''
    print(report_name.upper())

    '''
        3. Create a new descending sorted list without changing sales.
    '''
    sorted_sales = sorted(sales, reverse = True)
    print(sorted_sales)
    '''
        4. Use indexing to obtain the largest and smallest sale.
    '''
    largest = sorted_sales[0]
    smallest = sorted_sales[-1]
    print(largest, smallest)

    '''
        5. Use slicing to obtain the top three.
    '''
    top_three = sorted_sales[:3]
    print(top_three)

    '''
        6. Use len() for the number of sales.
    '''
    length = len(sales)
    print(length)

    '''
        7. Use f-strings for the printed report
    '''
    print(f"{report_name.upper()} - {region}")
    print(f"Number of sales: {len(sales)}")
    print(f"Largest sale: ${largest:,.2f}")
    print(f"Smallest sale: ${smallest:,.2f}")
    print(f"Top three: {top_three}")

    '''
        8. Add one additional useful line of information of your own choosing.
    
    '''
    bottom_three = sorted_sales[-3:]
    print(f"Bottom Three: {bottom_three}")
question_d1()

# ============================================================
# PART E — COMPUTATIONAL THINKING REFLECTION
# ============================================================


def question_e1():
    """
    E1 — Computational Thinking Reflection

    Choose ONE:
        Abstraction
        Decomposition
        Pattern recognition
        Algorithms

    Identify one place in this exercise where you used that kind
    of thinking. Explain in 2–4 sentences what you did and why
    it fits that category.
    """

    # CHOSEN IDEA:
    # Pattern recognition

    # EXPLANATION:
    # In A3, B1, and C1, I kept running into the same idea: sorted() returns a
    # new list and leaves the original alone, while .sort() changes the original
    # list and returns None. Once I recognized that pattern, I could explain the
    # B1 bug (items = items.sort() saved None into items) and I knew to use
    # sorted() in C1 and D1 when the instructions said to leave sales unchanged.
    # This is pattern recognition because I noticed one rule repeating across
    # different problems and used it to predict what would happen in new ones.


# ============================================================
# RUN ONE QUESTION AT A TIME
# ============================================================

# Uncomment ONLY the question you are currently working on.
# Comment it again before moving to the next question.

# question_a1()
# question_a2()
# question_a3()
# question_b1()
# question_c1()
# question_d1()
# question_e1()
