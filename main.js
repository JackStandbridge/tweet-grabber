(d => {

let form = d.getElementById('js__usernameSelect'),
	input = form.querySelector('input'),
	title = d.getElementById('title');

const fetchTweets = e => {
	e.preventDefault();
	if (!input.value.length) {
		input.focus();
		return;
	};

	let list = d.getElementById('js__tweets');

	let xhr = new XMLHttpRequest();
	xhr.open('GET', `http://127.0.0.1:5000/${input.value}`);

	xhr.onload = () => {
		if (xhr.status === 200) {

			let tweets = JSON.parse(xhr.response);

			title.textContent = `${input.value}'s tweets:`

			// make new ul to replace old one
			let ul = d.createElement('ul');
			ul.id = 'js__tweets';

			// add each new tweet as an li to the ul
			tweets.forEach(tweet => {
				let li = d.createElement('li'),
					author = d.createElement('span'),
					time = d.createElement('time'),
					body = d.createElement('p');
				author.textContent = tweet.author;
				author.classList.add('author');
				time.textContent = tweet.time;
				body.textContent = tweet.body;
				[author, time, body].forEach(element => li.appendChild(element));
				ul.appendChild(li)
			});

			// replace ul and wipe form
			list.replaceWith(ul);
			input.value = '';
			input.focus();
		} else {
			alert('Request failed, status code: ', xhr.status)
		}
	};

	xhr.send()
}

form.addEventListener('submit', fetchTweets);

})(document);

