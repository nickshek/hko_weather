# HKO Weather

[![Software License](https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat-square)](LICENSE.md)

A simple library to get the hong kong weather information by reading [RSS feeds](http://rss.weather.gov.hk/rsse.html) provided by The Hong Kong Observatory

## Install

```python
pip install hko_weather
```

## Basic Usage

```python
import hko_weather
print(hko_weather.nine_days_forecast().text())
```

or execute ```hko_weather``` in linux terminal.

## Contributing

Feel free to submit any pull requests or add functionality

## License

The MIT License (MIT). Please see [License File](LICENSE.md) for more information.
