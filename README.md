# 📊 Library Usage Access Analytics System (IGCAR)

A centralized **Library Usage Access Analytics System** for the **Indira Gandhi Centre for Atomic Research (IGCAR)**.  
The system consolidates library service data (e.g., **auditorium bookings**, **eBook usage**) into **interactive dashboards**, helping staff and administrators with **evidence-based decision-making**.  

---

## 📖 Introduction  

The **IGCAR Library** provides diverse services like **auditorium bookings** and **eBook publishing**. These activities generate substantial data, but currently lack a **centralized analytics platform**.  

This project introduces a **Django-based system** that:  
- Imports raw CSV/Excel datasets into **MySQL**.  
- Visualizes data with **Chart.js** and **Plotly** dashboards.  
- Enables filtering, comparison, and custom analytics.  
- Helps optimize **resource allocation, trend analysis, and library operations**.  

---

## ⚠️ Problem Statement  

- Large amounts of **library usage data** remain underutilized.  
- Data exists in **Excel/CSV formats**, difficult to analyze manually.  
- No **centralized system** for administrators to monitor trends.  
- Difficulties in **resource planning, trend identification, and service optimization**.  

✅ **Proposed Solution**:  
A **Library Usage Analytics System** to:  
- Consolidate data from multiple services.  
- Provide **interactive dashboards**.  
- Allow **custom visualizations** by attributes (date, department, publisher, subject).  
- Support **real-time analysis and decision-making**.  

---

## 🔄 Workflow  

![System Workflow](afec2144-f12c-4688-b989-7b359827702f.png)  

**Steps**:  
1. Upload CSV/Excel dataset.  
2. Import into **MySQL Database** (via phpMyAdmin / XAMPP CMD).  
3. Django connects to MySQL (`settings.py` config).  
4. Auto-generate models with `inspectdb`.  
5. Build views & templates with MVT structure.  
6. Render dashboards with **Chart.js / Plotly**.  
7. Enable **user filters, dataset generation, and exports**.  

---

## 🏗️ System Components  

### 1. Data Source (Excel/CSV)  
- Input files contain fields like `sno`, `book_title`, `author`, `isbn`, `publisher`, `year`.  

### 2. Database (MySQL)  
- CSV imported via **phpMyAdmin** or **MySQL CMD**.  
- Central repository for analysis.  

### 3. Backend (Django)  
- Database configuration:  
  ```python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'website',
          'USER': 'root',
          'PASSWORD': '',
          'HOST': 'localhost',
          'PORT': '3306',
      }
  }

## 4. Views & Templates  

- **Views** handle queries & processing.  
- **Templates** display HTML/CSS/JS dashboards.  

---

## 5. Frontend Display  

- **Chart.js** → simple, responsive charts.  
- **Plotly** → advanced, 3D, interactive graphs.  

---

## 6. User Interaction  

- Filter by **date, department, publisher, subject**.  
- Generate reports dynamically.  
- Export data and visualizations.  
- Responsive UI with **Bootstrap/Tailwind CSS**.  

---

## 🗄️ Database Design  

### ER Observations  
- **Book Table** → auditorium/program data.  
- **Ebook Table** → digital book metadata.  
- **Primary Key** → `sno`.  
- Possible relationship: shared attributes like `title` and `author`.  

### Schema Example  

**Book Table**  
- `sno` (PK)  
- `reg_no`  
- `program_title`  
- `date`  
- `services`  
- `auditorium_name`  
- `requestor`  

**Ebook Table**  
- `sno` (PK)  
- `book_title`  
- `author`  
- `isbn`  
- `english_name`  
- `year_of_publish`  
- `publisher_name`  

---

## 📸 Screenshots  

### Home Page  
Displays **Library Usage Reports** with options for **Auditorium** and **Ebook Reports**.  

### Auditorium Dashboard  
- Event listings with **program title, venue, services, requestor**.  
- Searchable and sortable.  

### Visualization Tool  
- Select attributes and generate **bar/line/pie charts**.  

### Ebook Dashboard  
- Searchable eBook catalog with **title, author, year, publisher**.  

*(Insert screenshots of your actual project UI here)*  

---

## 🚀 Future Scope  

- **AI-powered recommendations** (suggest books/resources).  
- **Mobile App** (Android/iOS).  
- **RFID/QR support** for book issue/returns.  
- **Email/SMS alerts** for due dates & reservations.  
- **Role-based dashboards** (Admin, Librarian, Student).  
- **Cloud deployment** (AWS, Heroku).  
- **External integrations** with digital libraries/journals.  
- **Book reviews & ratings** by users.  
- **Multi-language & accessibility support**.  

---

## 🛠️ Tech Stack  

- **Backend:** Django (Python)  
- **Database:** MySQL (XAMPP/phpMyAdmin)  
- **Frontend:** HTML, CSS, JavaScript, Bootstrap/Tailwind  
- **Visualization:** Chart.js, Plotly  

---

## ⚡ Installation  

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-username/library-usage-analytics.git
   cd library-usage-analytics
2. Create & activate virtual environment
    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    venv\Scripts\activate      # Windows

3. Install dependencies
    pip install -r requirements.txt

4. Configure database in settings.py.

    Run migrations
    python manage.py migrate

6. Create superuser

   python manage.py createsuperuser

7. Start server

    python manage.py runserver

## 👨‍💻 Author  

Developed by **SHREYAAS**  
Library Usage Access Analytics Project – IGCAR  
