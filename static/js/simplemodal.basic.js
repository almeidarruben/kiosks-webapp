/*
 * SimpleModal Basic Modal Dialog
 * http://simplemodal.com
 *
 * Copyright (c) 2013 Eric Martin - http://ericmmartin.com
 *
 * Licensed under the MIT license:
 *   http://www.opensource.org/licenses/mit-license.php
 */

jQuery(function ($) {
	// Load dialog on page load
	//$('#basic-modal-content').modal();

	// Load contacts modal
	/*$('.contacts-modal').click(function (e) {
		$('#contacts-modal-content').modal({
			position: [90, 244],
		});

		return false;
	});*/

	// Load video modal
	$('.contacts-modal').click(function (e) {
		$('#video-modal-content').modal({
			position: [90, 100],
			minWidth: 800,
		});

		return false;
	});

	// News Details
	$('.news').click(function (e) {
		$('#news-modal-content').modal({
			position: [435, 830],
			minWidth: 500,
		});

		return false;
	});

	// Ficha Técnica
	$('.footer-links').click(function (e) {
		$('#fichat-modal-content').modal({
			position: [435, 0],
			minWidth: 1360,
			minHeight: 420,
		});

		return false;
	});

});