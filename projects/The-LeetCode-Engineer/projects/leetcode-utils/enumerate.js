
const cell_status = 0;
const cell_solution =2;
const cell_acceptance = 3;
const cell_difficulty = 4;
const cell_frequency = 5;

function getPageTextLinkSet() {
    const cell_title = 1;
    const table = document.querySelectorAll("div[role='table']")
    const tableRows = table[2].querySelectorAll("div[role='rowgroup']")
    const r = tableRows[0];

    for (const inner of r.children) {
        const title = inner.children[cell_title]
        const href = title.querySelectorAll("a");
        const titleText = href[0].innerText
        const link = href[0].href
        console.log("title: ", titleText, " link: ", link);
    }
}

function navigateNextPage() {
    const navBarSet = document.querySelectorAll("nav[role='navigation']")
    const navBar = navBarSet[0];
    for (const btn of navBar.children) {
        
        parseInt(btn.innerText);
    }
}

navigateNextPage();
