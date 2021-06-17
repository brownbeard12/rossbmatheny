let myCards = document.querySelectorAll('.content');
let rail = document.querySelector('.rail');
    
    document.addEventListener('click', function(self) {
        
        var ind;
        
        if (self.target.className === 'content') {
            self.target.velocity({ 'border-color' : ['red', 'white']}, {'duration' : '100'});
        } else if (self.target.parentNode.className === 'content') {
            self.target.parentNode.velocity({ 'border-color' : ['red', 'white']}, {'duration' : '100'});
        };
        
        myCards.forEach( function(myCard, index) {
            
            if (self.target === myCard || self.target.parentNode === myCard) {
                ind = index;
            };

        });
        
        for( i = 0; i < myCards.length; i++) {
            if (i === ind) {
                continue;
            }
            myCards[i].velocity({ 'border-color' : 'white' }, {'duration' : '100'})
        };            
            

        
        console.log(self.target, self.target.parentNode, ind);
                
        self.stopPropagation();
        
    });