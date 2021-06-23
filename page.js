let myCards = document.querySelectorAll('.card');
let rail = document.querySelector('.rail');
    
document.addEventListener('click', function(self) {
    
    var ind;
    var selected_node = self.target.parentNode.querySelector('.content-detail') !== null;
    var selected_parent = self.target.parentNode.parentNode.querySelector('.content-detail') !== null;
    
    if (self.target.className === 'content' && selected_node) {
        self.target.parentNode.querySelector('.content-detail').velocity({ 'display' : 'block', 'opacity' : ['1', '0'] }, { 'duration': '125' });
    } else if (self.target.parentNode.className === 'content' && selected_parent) {
        self.target.parentNode.parentNode.querySelector('.content-detail').velocity({ 'display' : 'block', 'opacity' : ['1', '0'] }, { 'duration': '125' });
    };
    
    myCards.forEach( function(myCard, index) {
        
        if (self.target.parentNode === myCard || self.target.parentNode.parentNode === myCard) {
            ind = index;
        };

    });
    
    for( i = 0; i < myCards.length; i++) {
        if (i === ind) {
            continue;
        };
        let selection = myCards[i].querySelector('.content-detail') !== null;
        if(selection) {        
            myCards[i].querySelector('.content-detail').velocity({ 'display' : 'none', 'opacity' : '0' }, { 'duration': '125' });
        };

    };            
    
    self.stopPropagation();
    
});