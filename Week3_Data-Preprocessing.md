## Week 3: Data Cleaning and Data Preprocessing Techniques

**Duration:** 3 Hours

**Language:** English

**Tools:** Python, Pandas, NumPy, Scikit-learn

---

## Learning Objectives

By the end of this lecture, students will be able to:

* Understand why data cleaning is essential before modeling
* Handle missing values using multiple strategies
* Detect and treat outliers
* Encode categorical variables correctly
* Apply feature scaling and normalization
* Build a basic preprocessing pipeline

---

## ⏱ Course Schedule (3 Hours)

---

## 🔹 Part 1 

### Why Data Cleaning and Preprocessing Matter

### 1. Raw Data vs Clean Data

* Raw data is:
  * incomplete
  * noisy
  * inconsistent
* Clean data improves:
  * model accuracy
  * training stability
  * interpretability

📌 **Key Concept**

> *“Garbage in, garbage out.”*

---

### 2. Data Cleaning vs Data Preprocessing

| Term               | Description                                      |
| ------------------ | ------------------------------------------------ |
| Data Cleaning      | Fixing data problems (missing, outliers, errors) |
| Data Preprocessing | Transforming data for models                     |

---

## 🔹 Part 2 

### Handling Missing Values

### 1. Identify Missing Data

<pre class="overflow-visible! px-0!" data-start="1357" data-end="1388"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>df.isnull().</span><span>sum</span><span>()
</span></span></code></div></div></pre>

### 2. Common Strategies

#### (1) Remove Data

<pre class="overflow-visible! px-0!" data-start="1436" data-end="1479"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>df.dropna()
df.dropna(axis=</span><span>1</span><span>)
</span></span></code></div></div></pre>

When to use:

* Small amount of missing data
* Missing completely at random

---

#### (2) Simple Imputation

<pre class="overflow-visible! px-0!" data-start="1589" data-end="1709"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>df[</span><span>"age"</span><span>].fillna(df[</span><span>"age"</span><span>].mean(), inplace=</span><span>True</span><span>)
df[</span><span>"gender"</span><span>].fillna(df[</span><span>"gender"</span><span>].mode()[</span><span>0</span><span>], inplace=</span><span>True</span><span>)
</span></span></code></div></div></pre>

* Numerical → mean / median
* Categorical → mode

---

#### (3) Scikit-learn Imputer

<pre class="overflow-visible! px-0!" data-start="1796" data-end="1941"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>from</span><span> sklearn.impute </span><span>import</span><span> SimpleImputer

imputer = SimpleImputer(strategy=</span><span>"mean"</span><span>)
df[[</span><span>"age"</span><span>]] = imputer.fit_transform(df[[</span><span>"age"</span><span>]])
</span></span></code></div></div></pre>

📌 Discuss medical data examples:

* Missing lab values
* Missing diagnoses

---

## 🔹 Part 3 

### Outlier Detection and Treatment

### 1. What is an Outlier?

* Extreme or abnormal value
* May be:
  * Data error
  * Rare but valid case

---

### 2. Statistical Methods

#### (1) Z-score

<pre class="overflow-visible! px-0!" data-start="2275" data-end="2350"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>from</span><span> scipy </span><span>import</span><span> stats
z_scores = stats.zscore(df[</span><span>"income"</span><span>])
</span></span></code></div></div></pre>

#### (2) IQR Method

<pre class="overflow-visible! px-0!" data-start="2372" data-end="2465"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>Q1 = df[</span><span>"income"</span><span>].quantile(</span><span>0.25</span><span>)
Q3 = df[</span><span>"income"</span><span>].quantile(</span><span>0.75</span><span>)
IQR = Q3 - Q1
</span></span></code></div></div></pre>

---

### 3. Handling Outliers

* Remove
* Cap (Winsorization)
* Transform (log scale)

<pre class="overflow-visible! px-0!" data-start="2553" data-end="2606"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>df[</span><span>"income"</span><span>] = np.log(df[</span><span>"income"</span><span>] + </span><span>1</span><span>)
</span></span></code></div></div></pre>

📌 Emphasize:

> Do NOT blindly remove outliers in medical data.

---

## 🔹 Part 4 

### Encoding Categorical Variables

### 1. Why Encoding is Needed

* Machine learning models require numerical input

---

### 2. Types of Categorical Data

| Type    | Example                     |
| ------- | --------------------------- |
| Nominal | Gender, Blood type          |
| Ordinal | Severity level, Stage I–IV |

---

### 3. Encoding Techniques

#### (1) Label Encoding (Ordinal)

<pre class="overflow-visible! px-0!" data-start="3034" data-end="3165"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>from</span><span> sklearn.preprocessing </span><span>import</span><span> LabelEncoder

le = LabelEncoder()
df[</span><span>"severity"</span><span>] = le.fit_transform(df[</span><span>"severity"</span><span>])
</span></span></code></div></div></pre>

⚠ Warning:

* Do NOT use Label Encoding for nominal data

---

#### (2) One-Hot Encoding (Nominal)

<pre class="overflow-visible! px-0!" data-start="3265" data-end="3317"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>pd.get_dummies(df, columns=[</span><span>"gender"</span><span>])
</span></span></code></div></div></pre>

or

<pre class="overflow-visible! px-0!" data-start="3322" data-end="3383"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>from</span><span> sklearn.preprocessing </span><span>import</span><span> OneHotEncoder
</span></span></code></div></div></pre>

---

## 🔹 Part 5 

### Feature Scaling and Preprocessing Pipeline

---

### 1. Feature Scaling

#### Standardization

<pre class="overflow-visible! px-0!" data-start="3516" data-end="3604"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>from</span><span> sklearn.preprocessing </span><span>import</span><span> StandardScaler
scaler = StandardScaler()
</span></span></code></div></div></pre>

#### Normalization

<pre class="overflow-visible! px-0!" data-start="3625" data-end="3685"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>from</span><span> sklearn.preprocessing </span><span>import</span><span> MinMaxScaler
</span></span></code></div></div></pre>

| Method         | When to Use                      |
| -------------- | -------------------------------- |
| StandardScaler | Distance-based models (KNN, SVM) |
| MinMaxScaler   | Neural Networks                  |

---

### 2. Simple Preprocessing Pipeline

<pre class="overflow-visible! px-0!" data-start="3856" data-end="4000"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>from</span><span> sklearn.pipeline </span><span>import</span><span> Pipeline

pipeline = Pipeline([
    (</span><span>"imputer"</span><span>, SimpleImputer()),
    (</span><span>"scaler"</span><span>, StandardScaler())
])</span></span></code></div></div></pre>
