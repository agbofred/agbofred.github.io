<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project Tracker App</title>
</head>
<body>
    <h1>Project Pulse Dashboard</h1>

        <div style="display: flex; gap: 20px;">
            @foreach($projects as $project)
                <div style="border: 1px solid #ccc; padding: 15px; border-radius: 8px;">
                    <h3>{{ $project->title }}</h3>
                    <p>Progress: {{ $project->progress }}%</p>
                    <div style="background: #eee; width: 100px; height: 10px;">
                        <div style="background: green; width: {{ $project->progress }}px; height: 10px;"></div>
                    </div>
                </div>
            @endforeach
        </div>
</body>
</html>