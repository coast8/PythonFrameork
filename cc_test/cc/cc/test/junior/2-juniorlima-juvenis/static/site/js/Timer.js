var Timer = function(options){
    this.options = this.optionsDefault = $.extend({}, {
        time: 7,
        angleInterval: 5,
        color: '#bbbbbb',
        //timeInterval: 100, calculated
        direction: true,
        autoStart: true
    }, options);

    this.optionsTransition = $.extend({}, {
        angleInterval: 12,
        color: '#bbbbbb',
        timeInterval: 1, 
        direction: false
    });
    
    this.options.timeInterval = (this.options.time * 1000) / (360 / this.options.angleInterval);
    this.angle = 0;
    this.raio = 3;
    this.pos = 10;
    this.setCanvas();
    this.drawCircle();
    if (this.options.autoStart){
        this.setPath();
        this.start();
    }
};
Timer.prototype.setCanvas = function(){
    this.canvas = Raphael("ticker_timer", 20, 20);
};

Timer.prototype.drawCircle = function(){
    var circleParams = {
        'stroke': this.options.color,
        'stroke-width': 1,
        'fill': '#ffffff'
    };
    this.canvas.circle(this.pos, this.pos, this.raio * 2).attr(circleParams);
};

Timer.prototype.setPath = function(){
    this.pathParams = {
        'stroke': this.options.color,
        'stroke-width': this.raio * 2
    };
    this.arc = this.canvas.path([
        'M', this.pos, this.pos - this.raio,
        'A', this.raio, this.raio, 0, 0, 1, this.pos + 1, this.pos - this.raio
    ].join(',') ).attr(this.pathParams);
};

Timer.prototype.start = function(){
    var self = this;
    this.pause();
    this._interval = setInterval(function(){
        self.update( self.count() );
    }, this.options.timeInterval);
};

Timer.prototype.pause = function(){
    clearInterval(this._interval);
};
    
Timer.prototype.stop = function(){
    this.pause();
    this.angle = 0;
    this.update(0);
};

Timer.prototype.update = function(angle){
	if( !this.arc ) return false; 
    var largeArcFlag = this.options.direction ? +(angle > 180) : +(angle < 180);
    var sweepFlag = this.options.direction ? 1 : 0;
    var a = (90 - angle) * Math.PI / 180;
    var x = this.pos + this.raio * Math.cos(a);
    var y = this.pos - this.raio * Math.sin(a);
    var path = [
        "M", this.pos, this.pos - this.raio, 
        "A", this.raio, this.raio, 0, largeArcFlag, sweepFlag, x, y
    ].join();
    this.arc.attr({'path': path}).attr(this.pathParams);
};

Timer.prototype.count = function(){
    var angleTotal = 360;
    this.angle = (this.angle + this.options.angleInterval) % angleTotal;

    if (this.angle === 0) {
        var ticker = this.options.ticker;
        //this.options = this.options.direction ? this.optionsTransition : this.optionsDefault;
        this.pause();
        this.start();
        //if (!this.options.direction) 
        ticker.call(this);
    }
    
    if (this.angle === 0)
        this.angle = 5;

    return this.angle;
};


if ($.browser.msie
    && parseInt($.browser.version, 10) <= 6
    ){
    Timer.prototype.setCanvas
    = Timer.prototype.drawCircle
    = Timer.prototype.setPath
    = Timer.prototype.update
    = function(){};
}
