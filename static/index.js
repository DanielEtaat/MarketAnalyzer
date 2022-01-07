function newSetting(e) {
    let setting = document.getElementById(`${e.id}-setting`);
    if (e.checked) {
        setting.classList.remove("hidden");
    } else {
        setting.classList.add("hidden");
    }
}