const form = document.getElementById("searchForm");
form.addEventListener("submit", function (e) {
form.action = form.action.split("#")[0] + "#listings";
});
