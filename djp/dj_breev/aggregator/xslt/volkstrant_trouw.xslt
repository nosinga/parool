<?xml version="1.0" encoding="utf-8"?>
<xsl:transform
        xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
        version="1.0">

    <xsl:output method="text" encoding="utf-8"/>

    <xsl:template match="text()"/>
    <xsl:template match="script"/>

    <xsl:template match="div[@id='art_box2']">
        <xsl:for-each select="p | text()">
            <xsl:value-of select="."/>
            <xsl:text>&#10;</xsl:text>
            <xsl:text>&#10;</xsl:text>
        </xsl:for-each>
    </xsl:template>
</xsl:transform>
