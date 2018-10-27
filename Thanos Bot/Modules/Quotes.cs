using Discord.Commands;
using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;

namespace Thanos_Bot.Modules
{
    public class Quotes : ModuleBase<SocketCommandContext>
    {
        [Command("quote")]
        public async Task QuoteAsync()
        {
            Random random = new Random();
            string quote = "";
            string quote1 = "Fun isn’t something one considers when balancing the universe. But this… does put a smile on my face.";
            string quote2 = "When I’m done, half of humanity will still exist. Perfectly balanced, as all things should be. I hope they remember you.";
            string quote3 = "You’re strong. But I could snap my fingers, and you’d all cease to exist.";
            string quote4 = "The end is near.";
            string quote5 = "Stark… you have my respect. I hope the people of Earth will remember you.";
            string quote6 = "You should have gone for the head.";
            string quote7 = "I know what it’s like to lose. To feel so desperately that you’re right, yet to fail nonetheless. Dread it. Run from it. Destiny still arrives. Or should I say, I have.";
            string quote8 = "You’re a great fighter, Gamora. Come. Let me help you.";
            string quote9 = "Going to bed hungry. Scrounging for scraps. Your planet was on the brink of collapse. I was the one who stopped that. You know what’s happened since then? The children born have known nothing but full bellies and clear skies. It’s a paradise.";
            string quote10 = "I’m the only one who knows that. At least I’m the only who has the will to act on it. For a time, you had that same will. As you fought by my side, daughter.";
            string quote11 = "I ignored my destiny once, I can not do that again. Even for you. I’m sorry Little one.";
            string quote12 = "With all six stones, I can simply snap my fingers, they would all cease to exist. I call that mercy.”";
            string quote13 = "Thanos: “Daughter.”\nGamora: “Did you do it ?”\nThanos: “Yes.”\nGamora: “What did it cost?”\nThanos: “Everything.”";
            string quote14 = "Your optimism is misplaced, Asgardian.";
            string quote15 = "You’re strong. Me… You’re generous. Me… But I never taught you to lie. That’s why you’re so bad at it. Where is the Soul Stone?";
            string quote16 = "The hardest choices require the strongest wills.";
            string quote17 = "You should choose your words wisely";
            string quote18 = "The Tesseract… or your brother’s head. I assume you have a preference?";

            int num = random.Next(18);

            if (num == 1)
                quote = quote1;
            else if (num == 2)
                quote = quote2;
            else if (num == 3)
                quote = quote3;
            else if (num == 4)
                quote = quote4;
            else if (num == 5)
                quote = quote5;
            else if (num == 6)
                quote = quote6;
            else if (num == 7)
                quote = quote7;
            else if (num == 8)
                quote = quote8;
            else if (num == 9)
                quote = quote9;
            else if (num == 10)
                quote = quote10;
            else if (num == 11)
                quote = quote11;
            else if (num == 12)
                quote = quote12;
            else if (num == 13)
                quote = quote13;
            else if (num == 14)
                quote = quote14;
            else if (num == 15)
                quote = quote15;
            else if (num == 16)
                quote = quote16;
            else if (num == 17)
                quote = quote17;
            else
                quote = quote18;

            await ReplyAsync(quote);
        }
    }
}
