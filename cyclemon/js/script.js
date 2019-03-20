$(document).ready(function () {
	var scrollLink = $('.scroll');
	scrollLink.click(function (e) {
		e.preventDefault();
		$('body, html').animate({
			scrollTop: $(this.hash).offset().top
		}, 10000);
	});

	$(window).scroll(function(){
		var scrollbarLocation = $(this).scrollTop();

		scrollLink.each(function(){
			var sectionOffset = $(this.hash).offset().top - 1000;
			if (sectionOffset <= scrollbarLocation) {
				$(this).parent().addClass('active');
				$('.active').css('opacity: 1');
				$(this).parent().siblings().removeClass('active');
			}
		})
	})
})