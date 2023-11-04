let inputEle = document.getElementById("searchInput");
let searchResultsEle = document.getElementById("searchResults");
let spinnerEle = document.getElementById("spinner");

function createAndAppendSearchResult(result) {
    let {
        title,
        link,
        description
    } = result;


    let resultItemEle = document.createElement("div");
    resultItemEle.classList.add("result-item");

    searchResultsEle.appendChild(resultItemEle);


    let resultTitleEle = document.createElement("a");
    resultTitleEle.classList.add(result - title);
    resultTitleEle.textContent = title;
    resultTitleEle.href = link;
    resultTitleEle.target = "_blank";

    resultItemEle.appendChild(resultTitleEle);

    let titleBreakEle = document.createElement("br");
    resultItemEle.appendChild(titleBreakEle);

    let urlEle = document.createElement("a");
    urlEle.classList.add("result-url");
    urlEle.href = link;
    urlEle.target = "_blank";
    urlEle.textContent = link;
    resultItemEle.appendChild(urlEle);

    let linebreakEle = document.createElement("br");
    resultItemEle.appendChild(linebreakEle);

    let desciptionEle = document.createElement("p");
    desciptionEle.classList.add("line-description");
    desciptionEle.textContent = description;
    resultItemEle.appendChild(desciptionEle);
}

function displayResults(searchResults) {
    spinnerEle.classList.toggle("d-none");
    for (let result of searchResults) {
        createAndAppendSearchResult(result);
    }
}

function searchWikipedia(event) {
    if (event.key === "Enter") {
        searchResultsEle.textContent = "";
        spinnerEle.classList.toggle("d-none");
        let searchInput = inputEle.value;
        console.log(searchInput);

        let url = "https://apis.ccbp.in/wiki-search?search=" + searchInput;
        let options = {
            method: "GET"
        }
        fetch(url, options)
            .then(function(response) {
                return response.json();
            })
            .then(function(jsonData) {
                console.log(jsonData);
                let {
                    search_results
                } = jsonData;
                displayResults(search_results);
            })
    }
}

inputEle.addEventListener("keydown", searchWikipedia);