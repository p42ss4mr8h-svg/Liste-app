from flask import Flask, render_template_string

app = Flask(__name__)

# Beispiel-Daten für die Liste
liste = [
    {"bewertung": "Gut", "name": "Beispiel 1", "info": "Das ist Info 1"},
    {"bewertung": "Schlecht", "name": "Beispiel 2", "info": "Das ist Info 2"},
    {"bewertung": "Mittel", "name": "Beispiel 3", "info": "Das ist Info 3"},
]

@app.route('/')
def home():
    html = """
    <!DOCTYPE html>
    <html lang="de">
    <head>
        <meta charset="UTF-8">
        <title>Anime Liste</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

            body {
                background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 25%, #0f0f23 50%, #16213e 75%, #0f0f23 100%);
                background-size: 400% 400%;
                animation: subtleMesh 60s ease-in-out infinite;
                color: #e2e8f0;
                font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                margin: 0;
                padding: 24px;
                line-height: 1.5;
                overflow-x: hidden;
                min-height: 100vh;
            }

            @keyframes subtleMesh {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }

            h1 {
                text-align: center;
                color: #00d4ff;
                font-size: 2.5em;
                margin-bottom: 32px;
                font-weight: 600;
                letter-spacing: -0.025em;
            }

            #headerContainer {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 32px;
            }

            #actionButtons {
                display: flex;
                gap: 12px;
                align-items: center;
            }

            #exportButton, #importButton {
                background: linear-gradient(135deg, #00d4ff, #0099cc);
                color: #ffffff;
                border: none;
                border-radius: 8px;
                padding: 10px 16px;
                font-size: 0.9em;
                font-weight: 500;
                font-family: 'Inter', sans-serif;
                cursor: pointer;
                transition: all 0.3s ease;
                box-shadow: 0 2px 8px rgba(0, 212, 255, 0.3);
            }

            #exportButton:hover, #importButton:hover {
                background: linear-gradient(135deg, #0099cc, #00d4ff);
                box-shadow: 0 4px 12px rgba(0, 212, 255, 0.4);
                transform: translateY(-1px);
            }

            #quickStats {
                display: flex;
                justify-content: space-around;
                align-items: center;
                background: rgba(22, 33, 62, 0.6);
                backdrop-filter: blur(12px);
                border-radius: 12px;
                padding: 16px 24px;
                border: 1px solid rgba(0, 212, 255, 0.2);
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
                transition: all 0.3s ease;
                flex: 1;
                margin-right: 16px;
            }

            #randomButton {
                background: linear-gradient(135deg, #00d4ff, #0099cc);
                color: #ffffff;
                border: none;
                border-radius: 12px;
                padding: 16px 24px;
                font-size: 1em;
                font-weight: 600;
                font-family: 'Inter', sans-serif;
                cursor: pointer;
                transition: all 0.3s ease;
                box-shadow: 0 4px 12px rgba(0, 212, 255, 0.3);
                text-transform: uppercase;
                letter-spacing: 0.05em;
            }

            #randomButton:hover {
                background: linear-gradient(135deg, #0099cc, #00d4ff);
                box-shadow: 0 6px 16px rgba(0, 212, 255, 0.4);
                transform: translateY(-2px);
            }

            #randomButton:active {
                animation: pulse 0.3s ease;
            }

            @keyframes pulse {
                0% { transform: scale(1); }
                50% { transform: scale(1.05); }
                100% { transform: scale(1); }
            }

            .stat {
                text-align: center;
                flex: 1;
            }

            .stat-value {
                font-size: 1.5em;
                font-weight: 600;
                color: #00d4ff;
                display: block;
            }

            .stat-label {
                font-size: 0.875em;
                color: #94a3b8;
                text-transform: uppercase;
                letter-spacing: 0.05em;
                margin-top: 4px;
            }

            #searchContainer {
                margin-bottom: 24px;
            }

            #searchInput::placeholder {
                color: #94a3b8;
            }

            #searchInput:focus {
                border-color: #00d4ff;
                box-shadow: 0 0 0 2px rgba(0, 212, 255, 0.2);
            }

            .stat {
                text-align: center;
                flex: 1;
            }

            .stat-value {
                font-size: 1.5em;
                font-weight: 600;
                color: #00d4ff;
                display: block;
            }

            .stat-label {
                font-size: 0.875em;
                color: #94a3b8;
                text-transform: uppercase;
                letter-spacing: 0.05em;
                margin-top: 4px;
            }

            .section {
                margin-bottom: 24px;
                background: rgba(22, 33, 62, 0.4);
                backdrop-filter: blur(8px);
                border-radius: 12px;
                padding: 20px;
                border: 1px solid rgba(15, 52, 96, 0.3);
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
                transition: all 0.3s ease;
            }

            .section.neu-section {
                background: rgba(26, 26, 35, 0.5);
                border-top: 1px solid #ffd700;
                position: relative;
            }

            .section.neu-section::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                height: 1px;
                background: linear-gradient(90deg, transparent, #ffd700, transparent);
            }

            .section h2 {
                color: #00d4ff;
                font-size: 1.25em;
                font-weight: 600;
                margin: 0 0 16px 0;
                letter-spacing: 0.025em;
            }

            .section.neu-section h2 {
                color: #ffd700;
                font-weight: 500;
            }

            table {
                width: 100%;
                border-collapse: collapse;
                margin: 0;
            }

            th {
                font-size: 0.75em;
                font-weight: 600;
                text-transform: uppercase;
                letter-spacing: 0.1em;
                color: #94a3b8;
                padding: 12px 16px;
                text-align: left;
                border-bottom: 1px solid rgba(15, 52, 96, 0.3);
            }

            td {
                padding: 16px;
                border-bottom: 1px solid rgba(15, 52, 96, 0.2);
                vertical-align: middle;
                transition: all 0.2s ease;
            }

            td[contenteditable]:focus {
                background-color: rgba(15, 52, 96, 0.3);
                outline: none;
                border-radius: 6px;
            }

            tr:hover td {
                background-color: rgba(15, 52, 96, 0.2);
            }

            /* Highlight animation */
            .highlight {
                animation: highlightGlow 1s ease-out;
            }

            @keyframes highlightGlow {
                0% { box-shadow: 0 0 0 0 rgba(255, 215, 0, 0.7); transform: scale(1); }
                50% { box-shadow: 0 0 20px 5px rgba(255, 215, 0, 0.4); transform: scale(1.02); }
                100% { box-shadow: 0 0 0 0 rgba(255, 215, 0, 0); transform: scale(1); }
            }

            /* Badge styles for Bewertung */
            .badge {
                display: inline-flex;
                align-items: center;
                padding: 4px 8px;
                border-radius: 12px;
                font-size: 0.875em;
                font-weight: 500;
                text-transform: uppercase;
                letter-spacing: 0.025em;
                transition: all 0.2s ease;
            }

            .badge.star-5 { background-color: #166534; color: #dcfce7; }
            .badge.star-4 { background-color: #15803d; color: #bbf7d0; }
            .badge.star-3 { background-color: #ca8a04; color: #fef3c7; }
            .badge.star-2 { background-color: #dc2626; color: #fecaca; }
            .badge.star-1 { background-color: #7f1d1d; color: #fca5a5; }

            .rewatch-cell {
                width: 120px;
                padding: 12px 8px;
                text-align: center;
            }

            .rewatch-control {
                display: inline-flex;
                align-items: center;
                justify-content: center;
                gap: 6px;
                padding: 4px 6px;
                border-radius: 999px;
                background: rgba(15, 52, 96, 0.35);
                font-size: 0.95em;
                color: #e2e8f0;
            }

            .rewatch-btn {
                width: 26px;
                height: 26px;
                border: none;
                border-radius: 8px;
                background: rgba(0, 212, 255, 0.18);
                color: #e2e8f0;
                cursor: pointer;
                display: inline-flex;
                align-items: center;
                justify-content: center;
                font-size: 0.95em;
                padding: 0;
            }

            .rewatch-btn:hover {
                background: rgba(0, 212, 255, 0.3);
            }

            .rewatch-value {
                min-width: 14px;
                display: inline-flex;
                align-items: center;
                justify-content: center;
            }

            .badge::before {
                content: '★';
                margin-right: 4px;
                font-size: 0.75em;
            }
        </style>
    </head>
    <body>
        <h1>Anime Liste</h1>
        <div id="headerContainer">
            <div id="quickStats">
                <div class="stat">
                    <span class="stat-value" id="totalAnime">0</span>
                    <div class="stat-label">Gesamt Anime</div>
                </div>
                <div class="stat">
                    <span class="stat-value" id="fiveStarPercent">0%</span>
                    <div class="stat-label">5-Sterne Anteil</div>
                </div>
                <div class="stat">
                    <span class="stat-value" id="lastAdded">-</span>
                    <div class="stat-label">Zuletzt hinzugefügt</div>
                </div>
            </div>
            <div id="actionButtons">
                <button id="exportButton">Daten exportieren</button>
                <button id="importButton">Daten importieren</button>
                <input type="file" id="importFile" accept=".json" style="display: none;">
                <button id="randomButton">Was soll ich schauen?</button>
            </div>
        </div>
        <div id="searchContainer">
            <input type="text" id="searchInput" placeholder="Suche nach Anime-Name..." style="width: 100%; padding: 12px; border-radius: 8px; border: 1px solid rgba(0, 212, 255, 0.3); background: rgba(22, 33, 62, 0.6); color: #e2e8f0; font-family: 'Inter', sans-serif; font-size: 1em; outline: none; transition: all 0.3s ease;">
        </div>
        <div id="listeContainer">
            <!-- Abschnitte werden hier dynamisch eingefügt -->
        </div>
        <script>
            const container = document.getElementById('listeContainer');

            function saveData() {
                const sections = container.querySelectorAll('.section');
                const data = [];
                sections.forEach(section => {
                    const rows = section.querySelectorAll('tr');
                    rows.forEach(row => {
                        const cells = row.querySelectorAll('td');
                        if (cells.length === 3 || cells.length === 4) {
                            const bew = cells[0].textContent.trim();
                            const name = cells[1].textContent.trim();
                            const info = cells[2].textContent.trim();
                            const rewatch = getRewatchValue(cells);
                            if (name !== '' && info !== '') {
                                data.push({
                                    bewertung: bew,
                                    name: name,
                                    info: info,
                                    rewatch: rewatch
                                });
                            }
                        }
                    });
                });
                localStorage.setItem('listeData', JSON.stringify(data));
            }

            function loadData() {
                let data = JSON.parse(localStorage.getItem('listeData') || '[]');
                if (data.length === 0) {
                    // Beispiel-Daten hinzufügen
                    data = [
                        {"bewertung": "5.0", "name": "Attack on Titan", "info": "Epischer Anime über Titanen", "rewatch": 1},
                        {"bewertung": "4.5", "name": "Death Note", "info": "Psychologischer Thriller", "rewatch": 1},
                        {"bewertung": "4.0", "name": "One Piece", "info": "Abenteuer auf hoher See", "rewatch": 1},
                        {"bewertung": "3.5", "name": "Naruto", "info": "Ninja-Abenteuer", "rewatch": 1},
                        {"bewertung": "2.0", "name": "Beispiel schlechter Anime", "info": "Nur ein Beispiel", "rewatch": 1}
                    ];
                    localStorage.setItem('listeData', JSON.stringify(data));
                }
                data.forEach(item => {
                    const value = parseInt(item.rewatch, 10);
                    item.rewatch = isNaN(value) ? 1 : Math.min(9, Math.max(1, value));
                });
                return data;
            }

            function getRewatchValue(cells) {
                if (cells.length < 4) return 1;
                const raw = cells[3].getAttribute('data-rewatch') || cells[3].textContent.trim();
                const value = parseInt(raw, 10);
                return isNaN(value) ? 1 : Math.min(9, Math.max(1, value));
            }

            function validateBewertung(cell) {
                const value = cell.textContent.trim();
                if (value === '') return true;
                const num = parseFloat(value);
                if (isNaN(num) || num < 1.0 || num > 5.0) {
                    alert('Bewertung muss eine Zahl zwischen 1.0 und 5.0 sein.');
                    cell.textContent = '';
                    return false;
                }
                cell.textContent = num.toFixed(1);
                return true;
            }

            function groupData(data) {
                const groups = {};
                for (let i = 1; i <= 5; i++) {
                    groups[i] = [];
                }
                const watchlist = [];
                data.forEach(item => {
                    const name = item.name ? item.name.trim() : '';
                    const info = item.info ? item.info.trim() : '';
                    if (name === '' || info === '') return;
                    const rating = item.bewertung ? item.bewertung.toString().trim() : '';
                    if (rating === '') {
                        watchlist.push({ bewertung: '', name, info });
                        return;
                    }
                    const bew = parseFloat(rating);
                    if (!isNaN(bew)) {
                        const group = Math.floor(bew);
                        if (group >= 1 && group <= 5) {
                            const rewatch = item.rewatch ? Math.min(9, Math.max(1, parseInt(item.rewatch, 10) || 1)) : 1;
                            groups[group].push({ bewertung: item.bewertung, name, info, rewatch });
                        }
                    }
                });
                // Sort each group's entries by numeric rating descending (highest first)
                for (let i = 1; i <= 5; i++) {
                    groups[i].sort((a, b) => {
                        const na = parseFloat(a.bewertung) || 0;
                        const nb = parseFloat(b.bewertung) || 0;
                        return nb - na;
                    });
                }
                return { groups, watchlist };
            }

            function renderSections(groups, watchlist) {
                container.innerHTML = '';
                // Neu section
                const neuSection = document.createElement('div');
                neuSection.className = 'section neu-section';
                const neuH2 = document.createElement('h2');
                neuH2.textContent = 'Neu';
                neuSection.appendChild(neuH2);

                const neuTable = document.createElement('table');
                neuTable.innerHTML = `
                    <tr>
                        <th>Bewertung</th>
                        <th>Name</th>
                        <th>Info</th>
                    </tr>
                `;
                const neuRow = document.createElement('tr');
                neuRow.innerHTML = `
                    <td contenteditable="true" data-rating=""></td>
                    <td contenteditable="true"></td>
                    <td contenteditable="true"></td>
                `;
                neuTable.appendChild(neuRow);
                neuSection.appendChild(neuTable);
                container.appendChild(neuSection);

                if (watchlist.length > 0) {
                    const watchSection = document.createElement('div');
                    watchSection.className = 'section';
                    const watchH2 = document.createElement('h2');
                    watchH2.textContent = 'Watchlist';
                    watchH2.style.color = '#00d4ff';
                    watchSection.appendChild(watchH2);

                    const watchTable = document.createElement('table');
                    watchTable.innerHTML = `
                        <tr>
                            <th>Bewertung</th>
                            <th>Name</th>
                            <th>Info</th>
                        </tr>
                    `;
                    watchlist.forEach(item => {
                        const row = document.createElement('tr');
                        row.innerHTML = `
                            <td contenteditable="true" data-rating=""></td>
                            <td contenteditable="true">${item.name}</td>
                            <td contenteditable="true">${item.info}</td>
                        `;
                        watchTable.appendChild(row);
                    });

                    watchSection.appendChild(watchTable);
                    container.appendChild(watchSection);
                }

                // Other sections
                for (let i = 5; i >= 1; i--) {
                    if (groups[i].length > 0) {
                        const section = document.createElement('div');
                        section.className = 'section';
                        const h2 = document.createElement('h2');
                        h2.textContent = `${i} Sterne Anime`;
                        h2.style.color = '#00d4ff';
                        section.appendChild(h2);

                        const table = document.createElement('table');
                        table.innerHTML = `
                            <tr>
                                <th>Bewertung</th>
                                <th>Name</th>
                                <th>Info</th>
                                <th></th>
                            </tr>
                        `;
                        groups[i].forEach(item => {
                            const row = document.createElement('tr');
                            const rating = parseFloat(item.bewertung);
                            const starClass = `star-${Math.floor(rating)}`;
                            const rewatch = item.rewatch ? Math.min(9, Math.max(1, parseInt(item.rewatch, 10) || 1)) : 1;
                            row.innerHTML = `
                                <td contenteditable="true" data-rating="${item.bewertung}"><span class="badge ${starClass}">${item.bewertung}</span></td>
                                <td contenteditable="true">${item.name}</td>
                                <td contenteditable="true">${item.info}</td>
                                <td class="rewatch-cell" data-rewatch="${rewatch}">
                                    <div class="rewatch-control">
                                        <button type="button" class="rewatch-btn decrement">-</button>
                                        <span class="rewatch-value">${rewatch}</span>
                                        <button type="button" class="rewatch-btn increment">+</button>
                                    </div>
                                </td>
                            `;
                            table.appendChild(row);
                        });

                        section.appendChild(table);
                        container.appendChild(section);
                    }
                }
            }

            function updateDisplay() {
                const data = loadData();
                const { groups, watchlist } = groupData(data);
                renderSections(groups, watchlist);
                // Update stats
                const total = data.length;
                const fiveStarCount = data.filter(item => Math.floor(parseFloat(item.bewertung)) === 5).length;
                const fiveStarPercent = total > 0 ? Math.round((fiveStarCount / total) * 100) : 0;
                const lastAdded = localStorage.getItem('lastAdded') || '-';
                document.getElementById('totalAnime').textContent = total;
                document.getElementById('fiveStarPercent').textContent = `${fiveStarPercent}%`;
                document.getElementById('lastAdded').textContent = lastAdded;
                // Apply current search filter
                const searchInput = document.getElementById('searchInput');
                filterRows(searchInput.value);
            }

            function isRowComplete(row) {
                const cells = row.querySelectorAll('td');
                return Array.from(cells).every(cell => cell.textContent.trim() !== '');
            }

            function isWatchlistCandidate(row) {
                const cells = row.querySelectorAll('td');
                const rating = cells[0].textContent.trim();
                const name = cells[1].textContent.trim();
                const info = cells[2].textContent.trim();
                return rating === '' && name !== '' && info !== '';
            }

            function moveRowToWatchlist(row) {
                const cells = row.querySelectorAll('td');
                const item = {
                    bewertung: '',
                    name: cells[1].textContent.trim(),
                    info: cells[2].textContent.trim()
                };
                const data = loadData();
                data.push(item);
                localStorage.setItem('listeData', JSON.stringify(data));
                localStorage.setItem('lastAdded', item.name);
                cells[0].textContent = '';
                cells[1].textContent = '';
                cells[2].textContent = '';
                updateDisplay();
                setTimeout(() => {
                    const sections = container.querySelectorAll('.section');
                    sections.forEach(section => {
                        if (section.querySelector('h2').textContent === 'Watchlist') {
                            const rows = section.querySelectorAll('tr');
                            for (let i = 1; i < rows.length - 1; i++) {
                                const nameCell = rows[i].querySelectorAll('td')[1];
                                if (nameCell && nameCell.textContent.trim() === item.name) {
                                    rows[i].classList.add('highlight');
                                    setTimeout(() => rows[i].classList.remove('highlight'), 1000);
                                    break;
                                }
                            }
                        }
                    });
                }, 100);
            }

            function removeWatchlistItem(item) {
                const data = loadData();
                const filtered = data.filter(entry => {
                    const entryRating = entry.bewertung ? entry.bewertung.toString().trim() : '';
                    const isWatchlistEntry = entryRating === '';
                    const sameName = entry.name.trim() === item.name.trim();
                    const sameInfo = entry.info.trim() === item.info.trim();
                    return !(isWatchlistEntry && sameName && sameInfo);
                });
                localStorage.setItem('listeData', JSON.stringify(filtered));
            }

            function moveRowToGroup(row, removeExisting = false) {
                const cells = row.querySelectorAll('td');
                const bew = parseFloat(cells[0].textContent.trim());
                if (!isNaN(bew) && bew >= 1 && bew <= 5) {
                    const group = Math.floor(bew);
                    const rewatch = getRewatchValue(cells);
                    const item = {
                        bewertung: cells[0].textContent.trim(),
                        name: cells[1].textContent.trim(),
                        info: cells[2].textContent.trim(),
                        rewatch: rewatch
                    };
                    // Add to data
                    const data = loadData();
                    if (removeExisting) {
                        removeWatchlistItem(item);
                    }
                    data.push(item);
                    localStorage.setItem('listeData', JSON.stringify(data));
                    localStorage.setItem('lastAdded', item.name);
                    // Clear the row
                    cells[0].textContent = '';
                    cells[1].textContent = '';
                    cells[2].textContent = '';
                    // Update display
                    updateDisplay();
                    // Highlight the new row
                    setTimeout(() => {
                        const sections = container.querySelectorAll('.section');
                        sections.forEach(section => {
                            if (section.querySelector('h2').textContent === `${group} Sterne Anime`) {
                                const rows = section.querySelectorAll('tr');
                                // Find the row with the matching name
                                for (let i = 1; i < rows.length - 1; i++) { // Skip header and last empty
                                    const nameCell = rows[i].querySelectorAll('td')[1];
                                    if (nameCell && nameCell.textContent.trim() === item.name) {
                                        rows[i].classList.add('highlight');
                                        setTimeout(() => rows[i].classList.remove('highlight'), 1000);
                                        break;
                                    }
                                }
                            }
                        });
                    }, 100);
                }
            }

            container.addEventListener('focus', function(e) {
                if (e.target.tagName === 'TD' && e.target.hasAttribute('data-rating')) {
                    const rating = e.target.getAttribute('data-rating');
                    e.target.textContent = rating;
                    e.target.style.textAlign = 'left';
                }
            }, true);

            container.addEventListener('blur', function(e) {
                if (e.target.tagName === 'TD') {
                    const row = e.target.parentNode;
                    const section = row.closest('.section');
                    const cellIndex = Array.from(e.target.parentNode.children).indexOf(e.target);
                    if (cellIndex === 0) { // Bewertung column
                        if (!validateBewertung(e.target)) return;
                        // Render badge
                        const rating = e.target.textContent.trim();
                        if (rating) {
                            const numRating = parseFloat(rating);
                            const starClass = `star-${Math.floor(numRating)}`;
                            e.target.innerHTML = `<span class="badge ${starClass}">${rating}</span>`;
                            e.target.setAttribute('data-rating', rating);
                        } else {
                            e.target.innerHTML = '';
                            e.target.setAttribute('data-rating', '');
                        }
                    }
                    if (section.querySelector('h2').textContent === 'Neu') {
                        if (isWatchlistCandidate(row)) {
                            moveRowToWatchlist(row);
                        } else if (isRowComplete(row)) {
                            moveRowToGroup(row);
                        }
                    } else if (section.querySelector('h2').textContent === 'Watchlist') {
                        const cells = row.querySelectorAll('td');
                        const rating = cells[0].textContent.trim();
                        if (rating !== '' && isRowComplete(row)) {
                            moveRowToGroup(row, true);
                        } else {
                            saveData();
                            updateDisplay();
                        }
                    } else {
                        // Nur für andere Abschnitte speichern und anzeigen
                        saveData();
                        updateDisplay();
                    }
                }
            }, true);

            container.addEventListener('click', function(e) {
                if (e.target.matches('.rewatch-btn')) {
                    const cell = e.target.closest('.rewatch-cell');
                    if (!cell) return;
                    const valueSpan = cell.querySelector('.rewatch-value');
                    let value = parseInt(valueSpan.textContent, 10);
                    if (isNaN(value)) value = 1;
                    if (e.target.classList.contains('increment')) {
                        value = Math.min(9, value + 1);
                    } else if (e.target.classList.contains('decrement')) {
                        value = Math.max(1, value - 1);
                    }
                    valueSpan.textContent = value;
                    cell.setAttribute('data-rewatch', value);
                    saveData();
                }
            });

            function filterRows(query) {
                const sections = container.querySelectorAll('.section');
                sections.forEach(section => {
                    const rows = section.querySelectorAll('tr');
                    let hasVisibleRows = false;
                    rows.forEach((row, index) => {
                        if (index === 0) return; // Skip header
                        const cells = row.querySelectorAll('td');
                        if (cells.length >= 3) {
                            const name = cells[1].textContent.trim().toLowerCase();
                            const info = cells[2].textContent.trim().toLowerCase();
                            let matches = false;
                            if (query === '') {
                                matches = true;
                            } else {
                                matches = name.includes(query.toLowerCase()) || info.includes(query.toLowerCase());
                            }
                            row.style.display = matches ? '' : 'none';
                            if (matches && index > 0) { // Any data row (not header)
                                hasVisibleRows = true;
                            }
                        }
                    });
                    // Always show the last empty row if it's the neu-section
                    if (section.classList.contains('neu-section')) {
                        const lastRow = rows[rows.length - 1];
                        if (lastRow) lastRow.style.display = '';
                        hasVisibleRows = true;
                    }
                    // Hide section if no visible rows
                    section.style.display = hasVisibleRows ? '' : 'none';
                });
            }

            // Export/Import functionality
            const exportButton = document.getElementById('exportButton');
            const importButton = document.getElementById('importButton');
            const importFile = document.getElementById('importFile');

            exportButton.addEventListener('click', () => {
                const data = loadData();
                const lastAdded = localStorage.getItem('lastAdded') || '';
                const exportData = { listeData: data, lastAdded: lastAdded };
                const blob = new Blob([JSON.stringify(exportData, null, 2)], { type: 'application/json' });
                const url = URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = 'anime-liste-backup.json';
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
                URL.revokeObjectURL(url);
            });

            importButton.addEventListener('click', () => {
                importFile.click();
            });

            importFile.addEventListener('change', (e) => {
                const file = e.target.files[0];
                if (file) {
                    const reader = new FileReader();
                    reader.onload = (event) => {
                        try {
                            const importData = JSON.parse(event.target.result);
                            if (importData.listeData && Array.isArray(importData.listeData)) {
                                localStorage.setItem('listeData', JSON.stringify(importData.listeData));
                                if (importData.lastAdded) {
                                    localStorage.setItem('lastAdded', importData.lastAdded);
                                }
                                updateDisplay();
                                alert('Daten erfolgreich importiert!');
                            } else {
                                alert('Ungültige Datei!');
                            }
                        } catch (error) {
                            alert('Fehler beim Importieren: ' + error.message);
                        }
                    };
                    reader.readAsText(file);
                }
            });

            const randomButton = document.getElementById('randomButton');

            randomButton.addEventListener('click', () => {
                const data = loadData();
                const highRated = data.filter(item => {
                    const rating = parseFloat(item.bewertung);
                    return rating >= 4.0;
                });
                if (highRated.length > 0) {
                    const randomItem = highRated[Math.floor(Math.random() * highRated.length)];
                    // Find the row
                    const sections = container.querySelectorAll('.section');
                    let found = false;
                    for (const section of sections) {
                        if (section.querySelector('h2').textContent.includes('Sterne Anime')) {
                            const rows = section.querySelectorAll('tr');
                            for (let i = 1; i < rows.length - 1; i++) { // Skip header and last empty
                                const nameCell = rows[i].querySelectorAll('td')[1];
                                if (nameCell && nameCell.textContent.trim() === randomItem.name) {
                                    rows[i].scrollIntoView({ behavior: 'smooth', block: 'center' });
                                    rows[i].classList.add('highlight');
                                    setTimeout(() => rows[i].classList.remove('highlight'), 1500);
                                    found = true;
                                    break;
                                }
                            }
                            if (found) break;
                        }
                    }
                } else {
                    alert('Keine hoch bewerteten Animes gefunden!');
                }
            });

            // Search functionality
            const searchInput = document.getElementById('searchInput');
            searchInput.addEventListener('input', (e) => {
                filterRows(e.target.value);
            });

            // Initial load
            updateDisplay();
        </script>
    </body>
    </html>
    """
    return render_template_string(html, liste=liste)

if __name__ == '__main__':
    app.run(debug=True)
