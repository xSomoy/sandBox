chrome.tabs.onActivated.addListener(tab => {
    chrome.tabs.get(tab.tabId, current_Tab_Info => {
        if(/^https:\/\/www\.bohubrihi/.test(current_Tab_Info.url)) {
            chrome.tabs.executeScript(null, {file:'./skip.js'}, ()=> console.log('i injected'))
        }

    });
});
//console.log('test');
