/*
 * Selling Partner API for Fulfillment Inbound
 * The Selling Partner API for Fulfillment Inbound lets you create applications that create and update inbound shipments of inventory to Amazon's fulfillment network.
 *
 * OpenAPI spec version: v0
 *
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

package software.amazon.spapi.models.fulfillment.inbound.v0;

import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import java.io.IOException;

/** Where the seller provided box contents information for a shipment. */
@JsonAdapter(BoxContentsSource.Adapter.class)
public enum BoxContentsSource {
    @SerializedName("NONE")
    NONE("NONE"),
    @SerializedName("FEED")
    FEED("FEED"),
    @SerializedName("2D_BARCODE")
    _2D_BARCODE("2D_BARCODE"),
    @SerializedName("INTERACTIVE")
    INTERACTIVE("INTERACTIVE");

    private String value;

    BoxContentsSource(String value) {
        this.value = value;
    }

    public String getValue() {
        return value;
    }

    @Override
    public String toString() {
        return String.valueOf(value);
    }

    public static BoxContentsSource fromValue(String input) {
        for (BoxContentsSource b : BoxContentsSource.values()) {
            if (b.value.equals(input)) {
                return b;
            }
        }
        return null;
    }

    public static class Adapter extends TypeAdapter<BoxContentsSource> {
        @Override
        public void write(final JsonWriter jsonWriter, final BoxContentsSource enumeration) throws IOException {
            jsonWriter.value(String.valueOf(enumeration.getValue()));
        }

        @Override
        public BoxContentsSource read(final JsonReader jsonReader) throws IOException {
            Object value = jsonReader.nextString();
            return BoxContentsSource.fromValue((String) (value));
        }
    }
}
