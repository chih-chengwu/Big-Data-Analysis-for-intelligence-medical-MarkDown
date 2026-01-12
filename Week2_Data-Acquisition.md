## Week 2: Data Acquisition and Data Understanding with Pandas

**Duration:** 3 hours

**Language:** English

**Tools:** Python, Pandas, Jupyter Notebook / Colab

---

## Learning Objectives (What students will learn)

By the end of this lecture, students will be able to:

* Understand the role of data acquisition in the data science pipeline
* Load data from common sources using Pandas
* Inspect and explore datasets systematically
* Identify data types, missing values, and basic data quality issues
* Perform initial data understanding before modeling

---

## ⏱ Course Structure (3 Hours)

---

## 🔹 Part 1

### Introduction to Data Acquisition

### 1. What is Data Acquisition?

* Definition: collecting and importing data for analysis
* Why data acquisition is critical in AI & data science
* Real-world examples:
  * Medical records
  * Medical images (X-ray metadata, labels)
  * Insurance claim datasets
  * Open datasets (Kaggle, UCI, government data)

### 2. Common Data Sources

* CSV files
* Excel files
* Databases (conceptual overview only)
* APIs (conceptual overview)
* Image datasets (labels + metadata, not images yet)

📌 **Key Message:**

> *“A model is only as good as the data you feed it.”*

---

## 🔹 Part 2

### Introduction to Pandas

### 1. What is Pandas?

* Python library for data manipulation and analysis
* Core data structures:
  * `Series`
  * `DataFrame`

### 2. Importing Pandas

<pre class="overflow-visible! px-0!" data-start="1644" data-end="1677"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>import</span><span> pandas </span><span>as</span><span> pd
</span></span></code></div></div></pre>

### 3. Loading Data with Pandas

* Read CSV file

<pre class="overflow-visible! px-0!" data-start="1727" data-end="1769"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>df = pd.read_csv(</span><span>"data.csv"</span><span>)
</span></span></code></div></div></pre>

* Read Excel file

<pre class="overflow-visible! px-0!" data-start="1789" data-end="1834"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>df = pd.read_excel(</span><span>"data.xlsx"</span><span>)
</span></span></code></div></div></pre>

* Common parameters:
  * `sep`
  * `header`
  * `encoding`

### 4. First Look at the Dataset

<pre class="overflow-visible! px-0!" data-start="1929" data-end="1982"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>df.head()
df.tail()
df.shape
df.columns
</span></span></code></div></div></pre>

📌 Explain:

* Rows = samples
* Columns = features
* Observations vs variables

---

## 🔹 Part 3 

### Data Understanding: Structure and Types

### 1. Understanding Data Types

<pre class="overflow-visible! px-0!" data-start="2205" data-end="2238"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>df.dtypes
df.info()
</span></span></code></div></div></pre>

Explain common types:

* `int64`, `float64`
* `object`
* `bool`
* `datetime`

### 2. Why Data Types Matter

* Memory usage
* Mathematical operations
* Model compatibility

### 3. Descriptive Statistics

<pre class="overflow-visible! px-0!" data-start="2440" data-end="2467"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>df.describe()
</span></span></code></div></div></pre>

Explain:

* mean
* std
* min / max
* quartiles

📌 Discuss:

* What looks “normal”?
* What looks suspicious?

---

## 🔹 Part 4 

### Data Quality Check

### 1. Missing Values

<pre class="overflow-visible! px-0!" data-start="2657" data-end="2700"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>df.isnull()
df.isnull().</span><span>sum</span><span>()
</span></span></code></div></div></pre>

* Why missing data happens
* Examples in medical data

### 2. Duplicated Data

<pre class="overflow-visible! px-0!" data-start="2780" data-end="2831"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>df.duplicated()
df.duplicated().</span><span>sum</span><span>()
</span></span></code></div></div></pre>

### 3. Simple Value Inspection

<pre class="overflow-visible! px-0!" data-start="2864" data-end="2937"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>df[</span><span>"column_name"</span><span>].value_counts()
df[</span><span>"column_name"</span><span>].unique()
</span></span></code></div></div></pre>

📌 Emphasize:

> Data understanding comes **before** data cleaning and modeling.

---

## 🔹 Part 5 

### Summary & Discussion

### Key Takeaways

* Data acquisition is the first step in any AI project
* Pandas is the standard tool for tabular data analysis
* Always inspect:
  * shape
  * data types
  * missing values
  * basic statistics
