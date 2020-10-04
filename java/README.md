# Java Client

<div dir="rtl">

برای نوشتن کد عامل به زبان جاوا، کلاسی با نام دل‌خواه تعریف کنید که از `BaseAgent` ارث‌بری می‌کند:

</div>

```java
import base.Action;
import base.AgentData;
import base.BaseAgent;
import base.TurnData;

public class Agent extends BaseAgent {

    public Agent() throws IOException {
        super();
    }

}
```

<div dir="rtl">

در این کلاس، شما باید متد `doTurn` را بازنویسی کنید. ورودی این متد، یک شئ از کلاس `TurnData` است و خروجی آن هم یک `Action`. به عنوان مثال، کد زیر همواره جهت پایین را برای حرکت عامل انتخاب می‌کند:

</div>

```java
import base.Action;
import base.AgentData;
import base.BaseAgent;
import base.TurnData;

public class Agent extends BaseAgent {

    public Agent() throws IOException {
        super();
    }

    @Override
    public Action doTurn(TurnData turnData) {
        return Action.DOWN;
    }

}
```

<div dir="rtl">

<strong>بسته‌ی `base` در فایل فشرده قرار دارد. آن را دانلود و در پروژه‌ی خود `import` کنید.</strong>

در شئ `turnData`، اطلاعات حالت فعلی محیط قرار دارد که شامل موارد زیر است:

<ul>
<li>عدد صحیح turnsLeft نشان‌گر تعداد نوبت‌های باقی‌مانده</li>
<li>آرایه‌ی agentData نگه‌دارنده‌ی اطلاعات عامل‌های محیط. هر عضو از نوع AgentData است</li>
<li>آرایه‌ی دوبعدی map که هر خانه یک رشته‌ی تک کاراکتری است و موجودیت‌های محیط (دیوار با                                          *، الماس با                                                   اعداد                                                      صحیح و پایگاه‌ها با حروف کوچک) را نشان می‌دهد.</li>
</ul>

برای هر عامل نیز در آرایه‌ی `agentData`، یک شئ حاوی اطلاعات زیر قرار دارد:

<ul>
<li>رشته‌ی name که نام عامل به صورت یک حرف بزرگ انگلیسی است.</li>
<li>مکان عامل به صورت یک شئ از کلاس Position (حاوی سطر در row و ستون در column)</li>
<li>عدد صحیح carrying که الماسی که عامل در حال حمل آن است را نشان می‌دهد. اگر هیچ الماسی در دست عامل نباشد، مقدار null در این متغیر قرار                  می‌گیرد.</li>
<li>لیست collected حاوی اعداد الماس‌هایی که عامل به پایگاه‌هایش تحویل داده.</li>
</ul>

نام عامل شما در رشته‌ی `this.name` کلاسی که ارث‌بری می‌کنید ذخیره شده است.

برای اجرای عامل، یک شئ از کلاسی که تعریف کرده‌اید بسازید و متد play آن را فراخوانی کنید. پس از پایان بازی، نام عامل برنده در خروجی این متد قرار می‌گیرد. در صورتی که بازی برنده‌ای نداشته باشد، خروجی متد برابر `NOBODY` خواهد بود.

یک نمونه برنامه‌ی عامل که در هر نوبت، ابتدا اطلاعات محیط را چاپ کرده و سپس کنش را از ورودی می‌خواند در فایل `src/Agent.java` قابل مشاهده است. اگر این عامل را برای بررسی ویژگی‌های محیط اجرا می‌کنید، متغیر `decision_time_limit` سرور را افزایش دهید تا زمان تصمیم‌گیری قبل از ورود کنش توسط شما به پایان نرسد.

</div>
