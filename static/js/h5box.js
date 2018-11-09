function toTop() {
    var x = document.body.scrollTop || document.documentElement.scrollTop;
    var c = x/10;
    var timer = setInterval(function(){
        window.scrollTo(0,x-=c);
        if (x <= 0)
            clearInterval(timer);
    }, 1);
}
var Modal = function(nodeId){
    this.node = document.getElementById(nodeId);
    this.bindEvent();
};
Modal.prototype = {
    constructor: Modal,
    bindEvent: function(){
        var that = this;
        $(this.node).on('click', '.modal-close', function(){
            that.hide();
        });
        $('body').on('click', '.modal-cover', function(){
            that.hide();
        });
    },
    show: function() {
        //插入遮罩层
        var cover = document.createElement('div');
        cover.setAttribute('class', 'modal-cover');
        cover.setAttribute('style', 'width:'+document.body.clientWidth+'px;height:'+document.body.clientHeight+'px;');
        document.body.appendChild(cover);
        //显示modal
        var w = document.body.clientWidth / 2;
        var l = document.body.clientWidth / 4;
        this.node.style.width = w + 'px';
        this.node.style.left = l + 'px';
        this.node.style.display = "block";
        var top = window.screen.height/2-this.node.offsetHeight-80;
        if (top < 20) {
            top = 20;
        }
        this.node.style.top = top + 'px';
    },
    hide: function() {
        this.node.style.display = "none";
        var cover = document.getElementsByClassName('modal-cover');
        if (cover) {
            document.body.removeChild(cover[0]);
        }
    }
};
var ExtForm = function() {
    this.bindEvent();
};
ExtForm.prototype = {
    constructor: ExtForm,
    bindEvent: function() {
        $('.ext-radio').on('click', function(){
            var status = parseInt($(this).attr('data-val')) || 0;
            if (status == 0) {
                $(this).addClass('ext-radio-check').attr('data-val', 1);
            } else {
                $(this).removeClass('ext-radio-check').attr('data-val', 0);
            }
            $(this).find('.ext-radio-item').addClass('active');
            $(this).find('.ext-radio-item').eq(status).removeClass('active');
        });
    },
    isChecked: function(nodeId) {
        if ($(nodeId).attr('data-val') == '1') {
            return true;
        }
        return false;
    }
};