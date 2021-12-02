<h1 id="earley-algorithm">Алгоритм Эрли</h1>
</blockquote>
<h1 id="-arncpp">Гайд по запуску проекта</h1>
<h2 id="-pycharm">Как запустить проект через консоль</h2>
<details>
<summary><strong>Первый этап: установка python и pytest.
<h5 id="-python3-pygame-"><em>Если у вас уже установлен python3 и вы можете самостоятельно установить библиотеку pygame — пропустите этот этап</em></h5></summary>
<p><strong>1. Скачайте python3 с официального <a href="https://www.python.org/downloads/">сайта</a> и установите его.</strong>
<strong>2. Во время установки <em>обязательно</em> поставьте галочку &quot;Add Python 3.x to PATH&quot;.</strong>
<img src="https://python-scripts.com/wp-content/uploads/2018/06/win-install-dialog.40e3ded144b0.png" alt="add path screenshot"></p>
<p><strong>3. Когда установка закончится запустите консоль нажать комбинацию Win + R.
<p><strong>4. Установите pytest, если хотите посмотреть покрытие тестами.
</details>

<details><summary>Второй этап: скачивание и запуск проекта.</summary>
<p><strong>1. Скачайте проект с github любым удобным для вас способом.</strong></p>
<p><strong>2. В консоли перейдите в папку. 
<p><strong>3. Запустите проект.
</details>



<details><summary>Команды, которые нужно выполнить, для запуска через консоль:</summary>
<p><code>git clone https://github.com/arncpp/earley-algorithm.git</code></p>
<p><code>pip install pytest</code></p>
<p><code>cd</code></p>
<p><code>python main.py</code></p></details>
</details>
<h1 id="-">Использование алгоритма</h1>
<h3 id="-">Параметры ввода:</h3>
<ol>
<li><p>Нетерминалы записываются большими латинскими буквами, терминалы - маленькими. Пустое слово - 1 или пустая строка.</p>
</li>
<li><p>Стартовый символ нужно обозначать буквой S.</p>
</li>
<li><p>Среди нетерминалов не должно быть символа S&#39;.</p>
</li>
</ol>
<p><strong>Первая строка - количество правил в грамматике (n). Дальше n строк - правила грамматики. Последняя строка - слово, выводимость которого нужно проверить.</strong></p>
<p>Пример работы:</p>
<pre><code><span class="hljs-keyword">Input</span>:
3
S <span class="hljs-keyword">aS</span>
S a
S <span class="hljs-keyword">bS</span>
baaaaaaaaaaaaaaaa
Output:
YES

<span class="hljs-keyword">Input</span>:
3
S <span class="hljs-keyword">aS</span>
S     <span class="hljs-comment">// можно заменить на S 1</span>
S ba
abaaaaaaaaaaaaaaaa
Output:
<span class="hljs-keyword">NO</span>
</code></pre><p>Вывод:
YES - если слово выводится в КС-грамматике, NO - если не выводится.</p>
<p><strong>Запуск тестов с помощью команды <code>coverage run -m pytest .</code></strong></p>

