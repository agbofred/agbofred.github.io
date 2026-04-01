<div>
    <!-- Order your soul. Reduce your wants. - Augustine -->
    @props(['level'])

    @php
        $colors = [
            'High' => 'background: #fee2e2; color: #b91c1c;',
            'Medium' => 'background: #fef3c7; color: #92400e;',
            'Low' => 'background: #dcfce7; color: #166534;',
        ];
    @endphp

    <span style="padding: 5px 10px; border-radius: 20px; font-weight: bold; {{ $colors[$level] ?? '' }}">
        {{ $level }}
    </span>
</div>