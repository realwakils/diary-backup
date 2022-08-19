let notes = [];

function getMonthFromString(mon) {
	return new Date(Date.parse(mon + " 1, 2012")).getMonth()+1
}

function ensureZero(str) {
	return str.length === 1 ? 0 + str : str;
}

function handleNote(note) {
	const dateRaw = note.children.item(0).children.item(1).children;
	const year = dateRaw.item(2).innerText.trim().split(' ')[1];
	const month = getMonthFromString(dateRaw.item(0).innerText).toString();
	const day = dateRaw.item(1).innerText.trim().split('\n')[0];
	const date = `${year}_${ensureZero(month)}_${ensureZero(day)}`.trim();

	const text = note.children.item(1).children;
	const title = text.item(0).innerText.trim();
	const body = text.item(1).innerText.trim();
	notes.push({title, body, date});
}

async function handlePage(i) {
	console.log(`Fetching page ${i}...`);
	const page = await fetch(`https://www.writediary.com/notes?&p=${i}`);
	const text = await page.text();
	const parser = new DOMParser();
	const doc = parser.parseFromString(text, 'text/html');

	const rawNotes = [...doc.querySelectorAll('.frame')];
	rawNotes.forEach(handleNote);
}

function downloadData(object) {
	const anchor = document.createElement('a');
	anchor.id = "downloadAnchorElem"
	anchor.style = "display:none";
	document.body.appendChild(anchor);

	const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(object));
	const dlAnchorElem = document.getElementById('downloadAnchorElem');
	dlAnchorElem.setAttribute("href", dataStr);
	dlAnchorElem.setAttribute("download", "diary_backup.json");
	dlAnchorElem.click();
}

const amountOfPages = parseInt(document.querySelector('.page').innerText.split(' ')[3]);

console.log("Back up of all notes has just been initialized.");
for (let i = 1; i <= amountOfPages; i++) await handlePage(i);
console.log("Succesfully fetched all notes. There were notes from " + notes.length + " days.")

downloadData(notes);
console.log("Succesfully downloaded all notes. Please follow instructions in 'manual.txt'.");