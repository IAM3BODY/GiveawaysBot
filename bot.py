# Code Command [ without setting ]

@client.command()
@commands.has_permissions(manage_messages=True)
async def gstart(ctx, _time=None, *, prize=None):
  try:
    if _time is None:
      await ctx.reply('> **Please Type Time ..!**')
    elif prize is None:
      await ctx.reply('> Please Type Prize ..!')
    

    d = _time[-1]
    rl = int(_time[:-1])
    
    
    embed = discord.Embed(
      title = f'{ctx.guild.name} | Giveaway REACTION_EMOJI_HERE',
      description = f'**{prize}**\n**Hosted By : {ctx.author.mention}**',
      color=ctx.author.color
    )
    embed.set_footer(text=f'Giveaway Ends In {rl}{d}')
    await ctx.message.delete()
    giv = await ctx.send(embed=embed)
    await giv.add_reaction("REACTION_EMOJI_HERE")
    if d == "m":
      await asyncio.sleep(rl*60)
    elif d == "h":
      await asyncio.sleep(rl*3600)
    elif d == "d":
      await asyncio.sleep(rl*86400)

    _giv = await ctx.channel.fetch_message(giv.id)
    users = await _giv.reactions[0].users().flatten()
    users.pop(users.index(client.user))
    winner = random.choice(users)

    em = discord.Embed(title=f'REACTION_EMOJI_HERE | Giveaway Ended .', description=f'Congratulations {winner.mention} , You Won **__{prize}__** REACTION_EMOJI_HERE', color=winner.color)
    em.set_footer(text=f'Hosted By : {ctx.author.name}', icon_url=f'{ctx.author.avatar_url}')
    
    await giv.edit(embed=em)
  except:
    await ctx.send('> **You Don\'t Have Permissions To Create Giveaway [Administrator Permissions] .**')
  
