<x-layouts.app>
    <x-slot:title>My Active Tasks</x-slot>

    <h2>Task Timer Dashboard</h2>
    
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Task Name</th>
                <th>Priority</th>
                <th>Created At</th>
            </tr>
        </thead>
        <tbody>
            @foreach($tasks as $task)
            <tr>
                <td>{{ $task->id }}</td>
                <td>{{ $task->name }}</td>
                <td>
                    <x-priority-badge :level="$task->priority" />
                </td>
                <td>{{ $task->created_at->format('M d, Y') }}</td>
            </tr>
            @endforeach
        </tbody>
    </table>
</x-layouts.app>