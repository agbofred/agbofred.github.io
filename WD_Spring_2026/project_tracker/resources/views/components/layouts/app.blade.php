<!DOCTYPE html>
<html>
<head>
    <title>Task Dashboard</title>
    <style>
        body { font-family: sans-serif; padding: 40px; background: #f4f7f6; }
        table { width: 100%; border-collapse: collapse; background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        th, td { padding: 15px; text-align: left; border-bottom: 1px solid #eee; }
        th { background: #6366f1; color: white; }
        .badge { padding: 5px 10px; border-radius: 20px; font-size: 0.8em; font-weight: bold; }
        .High { background: #fee2e2; color: #b91c1c; }
        .Medium { background: #fef3c7; color: #92400e; }
        .Low { background: #dcfce7; color: #166534; }
    </style>
</head>
<body>
    <nav>
        <a href="/tasks">Tasks</a> | <a href="/dashboard">Dashboard</a>
    </nav>
    <main>
        {{$slot}}
    </main>

</body>
</html>