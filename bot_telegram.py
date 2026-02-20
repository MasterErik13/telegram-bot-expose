from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import asyncio
import os

TOKEN = os.environ.get("BOT_TOKEN")


#TOKEN = "8555453604:AAEq0pQGqxBRbx6P11txy8BfFgeWfSctLNo"

def google_drive_direct_link(link):
    """
    Converte un link di Google Drive tipo:
    https://drive.google.com/file/d/FILE_ID/view?usp=drivesdk
    in un link diretto compatibile con Telegram:
    https://drive.google.com/uc?export=download&id=FILE_ID
    """
    try:
        file_id = link.split("/d/")[1].split("/")[0]
        return f"https://drive.google.com/uc?export=download&id={file_id}"
    except IndexError:
        return None


# Handler per /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ciao! digita la password dello slave da esporre")

# Handler per i messaggi di testo
async def risposta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    testo = update.message.text.lower()
    
    if "ciao" in testo:
        await update.message.reply_text("Ciao, come va?????")
    
    if "speciale" in testo:
        url_foto = "https://drive.google.com/uc?export=view&id=13Z3V0SgF9W3V_fIp9P7qee_eQa-y0EPY"
        await update.message.reply_photo(photo=url_foto)
    '''
    if "alessandro" in testo:
        url_foto = "https://drive.google.com/uc?export=download&id=15X0fg8fx9fwbclKErg0Kt30Mxbb9nlbH"
        
        # Invia la foto
        msg = await update.message.reply_photo(photo=url_foto)
        
        # Aspetta 10 secondi (puoi cambiare)
        await asyncio.sleep(1.8)
        
        # Cancella il messaggio per tutti
        await msg.delete()
    '''
    if "valerio" in testo:
        drive_link = "https://drive.google.com/file/d/1yr_ffoIq0iGmvyy2_cR4XG_yqG5GjZHs/view?usp=drivesdk"
        url_foto = google_drive_direct_link(drive_link)
        if url_foto:
            msg = await update.message.reply_photo(photo=url_foto)
            await asyncio.sleep(1.8)
            await msg.delete()

    if "edoardo" in testo:
        drive_link = "https://drive.google.com/file/d/1yr_ffoIq0iGmvyy2_cR4XG_yqG5GjZHs/view?usp=drivesdk"
        url_foto = google_drive_direct_link(drive_link)
        if url_foto:
            msg = await update.message.reply_photo(photo=url_foto, protect_content=True)
            await asyncio.sleep(1.8)
            await msg.delete()

    if "antonio" in testo:
            drive_link = "https://drive.google.com/file/d/1BnfWFv7SQp-7qkLNKgmNTj7ihC6R1fIw/view?usp=drivesdk"
            url_foto = google_drive_direct_link(drive_link)
            if url_foto:
                msg = await update.message.reply_photo(photo=url_foto)
                await asyncio.sleep(1.8)
                await msg.delete()

    if "dellamonica0" in testo:
            drive_link = "https://drive.google.com/file/d/1VnhW222jRZR5jCpuTBgf3wMlVEN0KoRK/view?usp=drivesdk"
            url_foto = google_drive_direct_link(drive_link)
            if url_foto:
                msg = await update.message.reply_photo(photo=url_foto, protect_content=True)
                await asyncio.sleep(1.5)
                await msg.delete()
    
    if "ezzo1" in testo:
            drive_link = "https://drive.google.com/file/d/1ElpQ-DymKswUge-grxkoiFFAeojstzG2/view?usp=drivesdk"
            url_foto = google_drive_direct_link(drive_link)
            if url_foto:
                msg = await update.message.reply_photo(photo=url_foto, protect_content=True)
                await asyncio.sleep(2)
                await msg.delete()

# Creiamo l'applicazione
app = ApplicationBuilder().token(TOKEN).build()

# Aggiungiamo gli handler
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), risposta))

# Avviamo il bot
app.run_polling()
print ("fatto")