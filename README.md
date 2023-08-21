<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
  body {
    margin: 0;
    padding: 0;
    font-family: Arial, sans-serif;
  }

  .top-menu {
    background-color: #333;
    overflow: hidden;
  }

  .top-menu a {
    float: left;
    display: block;
    color: white;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
  }

  .top-menu a:hover {
    background-color: #555;
  }

  @media (max-width: 600px) {
    .top-menu a {
      float: none;
      display: block;
      text-align: left;
    }
  }
  .two-column-container {
    display: flex;
    justify-content: space-between;
  }

  .column {
    flex: 1;
    padding: 20px;
    border: 1px solid #ccc;
    box-sizing: border-box;
  }
</style>
<title>Top Menu Example</title>
</head>
<body>
  <div class="top-menu">
    <a href="#home">Home</a>
    <a href="#about">About</a>
    <a href="#services">Services</a>
    <a href="#contact">Contact</a>
  </div>

  <div class="content">
    <h1>Welcome to Our Website</h1>
    <div class="two-column-container">
        <div class="column">
            <img src="images/fredprofile.jpg" width="200">
            <p style="padding-left: 50px;"> <strong> Fred Agbo</strong>, PhD</p>
        </div>
        <div class="column">
            <h2>About me</h2>
            <p>
            Assistant Professor of Computer Science - 2023: Willamette University, Salem, OR, USA <br>
            PhD in Computer Science - 2022: University of Eastern Finland <br>
            MSc in Computer Science - 2017: University of Ilorin <br>
            BSc in Computer Science - 2013: University of Jos
            </p>
        </div>
    </div>
    <p>More content of the page.</p>
  </div>
</body>
</html>

## Welcome!

<div>
Intructor: <strong> Fred Agbo </strong> <br>
Hall: Ford Hall 102
</div>
<div>
Course Sylabus <a href="Lecture/slides/Ch0_1.html" target="_blank"> Download here </a>

</div>

### Syllabus 
<div>
The syllabus can be accessed <a href="https://willamette.edu/~esroberts/pykarel/reader/index.html"> here </a>
</div>
