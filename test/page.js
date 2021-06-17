let myCards = document.querySelectorAll('.content');
let rail = document.querySelector('.rail');
    
    document.addEventListener('click', function(self) {
        
        if (self.target.className === 'content') {
            self.target.velocity({ 'border-color' : ['blue', 'white']});
        } else if (self.target.parentNode.className === 'content') {
            self.target.parentNode.velocity({ 'border-color' : ['blue', 'white']});
        } else {
            myCards.forEach( function(myCard) {
                    myCard.velocity({ 'border-color' : 'white' });
            });
        }
        
        console.log(self.target);
        /*self.stopPropagation();*/
        
    });