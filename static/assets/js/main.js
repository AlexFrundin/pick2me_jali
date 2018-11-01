$(document).ready(function() {
	$('.languages-content').hide();
	$('.languages-select').click(function() {
		$('.languages-content').slideToggle();
		$('.languages-select span').toggleClass('rotate');
	});
	$('.languages-content_mob').hide();
	$('.languages-select_mob').click(function() {
		$('.languages-content_mob').slideToggle();
		$('.languages-select_mob span').toggleClass('rotate');
	});
	$('.mob-menu_wrapper').hide();
	$('.burger-menu').click(function() {
		$('.mob-menu_wrapper').fadeIn();
	});
	$('.mob-menu_close').click(function() {
		$('.mob-menu_wrapper').fadeOut();
	});

	$('.languages-reg_select').hide();
	$('.languages-reg').click(function() {
		$('.languages-reg_select').slideToggle();
		$('.languages-reg span').toggleClass('rotate');
	});

	$('#another-vehicle').hide();
	$('#radio').change(function() {
		if (this.checked) {
			$('#another-vehicle').fadeOut(700);
			$('#have-car').fadeIn(700);
		}
	});
	$('#radio2').change(function() {
		if (this.checked) {
			$('#have-car').fadeOut(700);
			$('#another-vehicle').fadeIn(700);
		}
	});


	$('.taxi-license').hide();
	$('#checkbox').change(function() {
		if (this.checked) {
			$('.taxi-license').fadeOut(600);
		} else {
			$('.taxi-license').fadeIn(600);
		}
	});
});